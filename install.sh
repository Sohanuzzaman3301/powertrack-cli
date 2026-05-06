#!/bin/bash
set -e

# Colors
GREEN='\033[0;32m'
NC='\033[0m'

echo -e "${GREEN}Installing powertrack-cli...${NC}"

# Create bin directory if it doesn't exist
mkdir -p "$HOME/.local/bin"

# Copy the script
cp powertrack.py "$HOME/.local/bin/powertrack"
chmod +x "$HOME/.local/bin/powertrack"

echo -e "${GREEN}Installation complete!${NC}"
echo "Make sure $HOME/.local/bin is in your PATH."
echo "You can now run 'powertrack' in your terminal."
