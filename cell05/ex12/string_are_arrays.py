import sys

if len(sys.argv) == 2:

    string = sys.argv[1]
    for i in string:
        if i == 'z':
            print('z', end='')
    print()
else:print("none")
