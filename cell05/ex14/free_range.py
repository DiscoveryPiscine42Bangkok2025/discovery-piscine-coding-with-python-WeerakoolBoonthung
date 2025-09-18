import sys

if len(sys.argv) == 3 :
    try:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        result = list(range(x, y+ 1))
        print(result)
    except ValueError:print("none")
    
else:
    print("none")