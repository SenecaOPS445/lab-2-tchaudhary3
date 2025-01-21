#!/usr/bin/env python3
import sys

# Check if exactly 2 arguments are provided
if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} name age")
    sys.exit()

# Assign arguments to variables
name = sys.argv[1]
age = sys.argv[2]

# Output the message
print(f"Hi {name}, you are {age} years old.")

