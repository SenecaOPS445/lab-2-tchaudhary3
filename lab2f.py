#!/usr/bin/env python3
# Author: Tania Chaudhary
# Author ID: tchaudhary3
# Date Created: 2025/01/21

import sys

# Validate that the required argument is provided
if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <timer_value>")
    sys.exit(1)

# Initialize the timer using the first command line argument
timer = int(sys.argv[1])

# Countdown loop
while timer > 0:
    print(timer)
    timer -= 1

# Print the final message
print("blast off!")
