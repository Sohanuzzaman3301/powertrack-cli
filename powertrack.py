#!/usr/bin/env python3
import os
import sys

def get_val(path):
    try:
        with open(path, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        return None

def format_time(hours):
    h = int(hours)
    m = int((hours - h) * 60)
    return f"{h}h {m}m"

def rainbow_text(text):
    colors = [
        "\033[38;5;196m", "\033[38;5;202m", "\033[38;5;208m", "\033[38;5;214m",
        "\033[38;5;220m", "\033[38;5;226m", "\033[38;5;190m", "\033[38;5;154m",
        "\033[38;5;118m", "\033[38;5;82m", "\033[38;5;46m", "\033[38;5;47m",
        "\033[38;5;48m", "\033[38;5;49m", "\033[38;5;50m", "\033[38;5;51m"
    ]
    res = ""
    for i, char in enumerate(text):
        res += colors[i % len(colors)] + char
    return res + "\033[0m"

def main():
    # Auto-detect battery
    base_path = "/sys/class/power_supply"
    batteries = [d for d in os.listdir(base_path) if d.startswith("BAT")]
    
    if not batteries:
        print("\033[31mError: No battery found in /sys/class/power_supply/\033[0m")
        sys.exit(1)
    
    bat_path = os.path.join(base_path, batteries[0])

    # Helper to get values with fallback
    def get_int(name):
        val = get_val(f"{bat_path}/{name}")
        return int(val) if val is not None else 0

    capacity = get_int("capacity")
    status = get_val(f"{bat_path}/status") or "Unknown"
    energy_now = get_int("energy_now")
    energy_full = get_int("energy_full")
    energy_full_design = get_int("energy_full_design")
    power_now = get_int("power_now")
    voltage_now = get_int("voltage_now") / 1000000

    power_w = power_now / 1000000
    energy_wh = energy_now / 1000000
    energy_full_wh = energy_full / 1000000
    energy_design_wh = energy_full_design / 1000000
    
    health = (energy_full / energy_full_design * 100) if energy_full_design > 0 else 0

    # Rainbow progress bar
    bar_width = 40
    filled = int(bar_width * capacity / 100)
    bar = ""
    for i in range(bar_width):
        if i < filled:
            # Gradient from Red to Green
            r = int(255 * (1 - i/bar_width))
            g = int(255 * (i/bar_width))
            bar += f"\033[38;2;{r};{g};0m█\033[0m"
        else:
            bar += "\033[90m░\033[0m"

    print(f"\n  {rainbow_text('⚡ BATTERY STATUS ⚡')}")
    print(f"  [{bar}] {capacity}%")
    print(f"  Status:       \033[1m{status}\033[0m")
    print(f"  Health:       \033[1m{health:.1f}%\033[0m ({energy_full_wh:.2f} / {energy_design_wh:.2f} Wh)")
    print(f"  Power Draw:   \033[38;5;214m{power_w:.2f} W\033[0m")
    print(f"  Voltage:      \033[38;5;117m{voltage_now:.2f} V\033[0m")

    if status == "Discharging" and power_w > 0:
        time_left = energy_wh / power_w
        print(f"  Time Empty:   \033[38;5;196m{format_time(time_left)}\033[0m")
    elif status == "Charging" and power_w > 0:
        time_to_full = (energy_full_wh - energy_wh) / power_w
        print(f"  Time Full:    \033[38;5;46m{format_time(time_to_full)}\033[0m")
    elif status == "Full":
        print(f"  Time Full:    \033[38;5;46mBattery is full\033[0m")
    
    print("")

if __name__ == "__main__":
    main()
