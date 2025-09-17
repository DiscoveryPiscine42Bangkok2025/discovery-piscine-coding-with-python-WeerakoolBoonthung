st_num = int(input("Enter a number less than 25\n"))
if(st_num>25):
    print("Error") 
else:
    for i in range(st_num, 26):
        print("Inside the loop, my variable is",i)
        i +=1
