import sys


if len(sys.argv) > 2:
    x =sys.argv[1:]
    x.reverse()
    for i in x:       
        print(i)
else:
    print("none")