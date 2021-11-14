#!/usr/bin/env python3

# Import the SHA256 Hash Algorithm
import sys
from passlib.hash import sha512_crypt

# Want a prompt instead of CLI?
# Comment out the "Grab from CLI" block.
# Then use this code instead to get a prompt:
#
# from getpass import getpass
# print "Type your desired password"
# password = getpass()

# Grab from CLI
if len(sys.argv) != 2:
  print("Please provide one argument: the plain-text password")
  exit()
password = sys.argv[1]

# Generate a new salt and hash the provided password
hash = sha512_crypt.hash(password);

# Output
print(hash)