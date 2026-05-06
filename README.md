# ⚡ powertrack-cli

![License](https://img.shields.io/github/license/Sohanuzzaman3301/powertrack-cli?style=flat-square)
![Release](https://img.shields.io/github/v/release/Sohanuzzaman3301/powertrack-cli?style=flat-square)
![Actions](https://img.shields.io/github/actions/workflow/status/Sohanuzzaman3301/powertrack-cli/release.yml?style=flat-square)

A vibrant, rainbow-infused battery and power monitor for your Linux terminal.

> [!TIP]
> **Add a GIF or Screenshot here!** Visuals are the best way to get people to try your terminal tools.

`powertrack` reads real-time data from your system's power supply class to give you a detailed breakdown of your battery health, power consumption, and time estimates, all wrapped in a beautiful gradient interface.

## ✨ Features

- 🌈 **Rainbow Gradient UI**: A smooth color-transition progress bar.
- 🔋 **Health Tracking**: Compares current capacity against original design capacity.
- ⚡ **Live Metrics**: Real-time power draw (Watts), voltage, and energy (Wh).
- ⏳ **Smart Estimates**: Calculates time until empty or full based on current usage.
- 🛠️ **Zero Dependencies**: Pure Python using built-in Linux `/sys/class/power_supply` APIs.

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/powertrack-cli.git
   cd powertrack-cli
   ```

2. **Make it executable:**
   ```bash
   chmod +x powertrack.py
   ```

3. **Install to your local bin:**
   ```bash
   mkdir -p ~/.local/bin
   cp powertrack.py ~/.local/bin/powertrack
   ```

## 💻 Usage

Simply run:
```bash
powertrack
```

## 📊 Example Output

```text
  ⚡ BATTERY STATUS ⚡
  [██████████████████████████████████████░░] 95%
  Status:       Discharging
  Health:       83.0% (66.38 / 80.00 Wh)
  Power Draw:   9.81 W
  Voltage:      16.86 V
  Time Empty:   6h 25m
```

## 📜 License
Distributed under the MIT License. See `LICENSE` for more information.
