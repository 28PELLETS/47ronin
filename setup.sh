#!/bin/bash

# 47 Ronin: The Automated Mechanic (V1)
# Built for the Oracle/Google Bunker - Jesse Candelaria (28pellets)

# 1. Update the Forge
sudo apt update && sudo apt upgrade -y

# 2. Install the Core (Python3)
sudo apt install python3 python3-pip python3-venv git -y

# 3. Clean the Shop (Removing any old clones)
rm -rf omni

# 4. Clone the Remote Vault (Using the GitHub Token)
# Note: You can also use SSH keys later, but for the first kick, use the Token.
git clone https://github.com/28PELLETS/47ronin.git omni

# 5. Move to the Shop
cd omni

# 6. Set up the Isolation Chamber (Virtual Environment)
python3 -m venv venv
source venv/bin/activate

# 7. Final Polish
chmod +x *.py

echo "Industrial Pulse: Status GREEN. The 47 Ronin are standing by."
