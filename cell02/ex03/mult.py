st_num = int(input("Enter the first number\n"))
nd_num = int(input("Enter the second number\n"))

X = st_num * nd_num
print(st_num,"x",nd_num,"=",X)
if(X==0): 
    print("The result is positive and negative.")
elif(X>0): 
    print("The result is positive.")
else: 
    print("The result is negative.")