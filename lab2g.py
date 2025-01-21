#!/usr/bin/env python3
# Author: Tania Chaudhary
# Author ID: tchaudhary3
# Date Created: 2025/01/21

import sys

# Check if a command line argument is provided
if len(sys.argv) == 2:
    timer = int(sys.argv[1])  # Use the provided argument for the timer
else:
    timer = 3  # Default value when no arguments are provided

# Countdown loop
while timer > 0:
    print(timer)
    timer -= 1

# Print the final message
print("blast off!")
