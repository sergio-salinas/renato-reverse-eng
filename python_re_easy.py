import sys

def verify(guess):
    vals = [ 83, 75, 89, 45, 79, 82, 68, 83, 45, 55, 57, 50, 54 ]
    
    if len(guess) != 13:
        return False

    for i, c in enumerate(guess):
        if ord(c) != vals[i]:
            return False
    return True

if len(sys.argv) != 1:
    print "Usage: python check.pyc"
    exit(1)

guess = raw_input("Enter your guess for the flag: ");

if verify(guess):
    print "That's the correct flag!"
else:
    print "Wrong flag."
