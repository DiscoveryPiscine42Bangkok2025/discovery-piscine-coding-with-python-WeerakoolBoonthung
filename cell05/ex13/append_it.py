import sys

if len(sys.argv) > 1:
    x =sys.argv[1:]
    ism = "ism"
    for i in x:
        last_three = i[-3:]
        if(last_three != ism):
            print(i+ism)
else:
    print("none")