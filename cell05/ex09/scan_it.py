import sys


if len(sys.argv) == 3:
    key = sys.argv[1]
    txt = sys.argv[2]
    count = txt.count(key)
    if count == 0:
        print("none")
    else:
        print(count)
else:
    print("none")  