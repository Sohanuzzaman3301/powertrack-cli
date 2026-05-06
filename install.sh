#!/bin/bash
set -e

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${BLUE}⚡ powertrack-cli Installer${NC}"

# Check for python3
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: python3 is not installed. Please install it first.${NC}"
    exit 1
fi

# Create bin directory if it doesn't exist
mkdir -p "$HOME/.local/bin"

# Determine source
if [ -f "powertrack.py" ]; then
    echo -e "Installing from local directory..."
    cp powertrack.py "$HOME/.local/bin/powertrack"
else
    echo -e "Downloading powertrack.py from GitHub..."
    curl -sSL https://raw.githubusercontent.com/Sohanuzzaman3301/powertrack-cli/main/powertrack.py -o "$HOME/.local/bin/powertrack"
fi

# Make it executable
chmod +x "$HOME/.local/bin/powertrack"

echo -e "${GREEN}✅ Installation complete!${NC}"

# Path check
if [[ ":$PATH:" != *":$HOME/.local/bin:"* ]]; then
    echo -e "${BLUE}Note:${NC} $HOME/.local/bin is not in your PATH."
    echo "Add this to your .bashrc or .zshrc:"
    echo -e "  ${BLUE}export PATH=\"\$HOME/.local/bin:\$PATH\"${NC}"
fi

echo -e "\nRun it with: ${GREEN}powertrack${NC}"
