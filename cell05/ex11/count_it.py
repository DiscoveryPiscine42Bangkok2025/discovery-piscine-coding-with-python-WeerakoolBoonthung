import sys

J=1

if len(sys.argv) > 1:   
    x =sys.argv[1:]
    print(f"parameters: {len(x)}")
    for i in x: 
        cti = len(i)
        print(f"{sys.argv[J]}: {cti}")
        J+=1
else:
    print("none")
#cd C:\Users\Administrator\Desktop\discovery_piscine\cell05\ex11   
#py count_it.py sawatdee kub eiei !!!!