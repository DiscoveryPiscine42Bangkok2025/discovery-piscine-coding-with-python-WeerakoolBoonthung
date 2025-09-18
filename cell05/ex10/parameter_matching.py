import sys


if len(sys.argv) == 2:
    key = sys.argv[1]
    regis = input("What was the parameter? ")
    if regis == key:
        print("Good job!")
    else:
        print("Nope, sory...")
else:
    print("none")  