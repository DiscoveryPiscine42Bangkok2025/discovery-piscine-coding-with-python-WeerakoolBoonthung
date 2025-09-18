a=[2,8,9,48,8,22,-12,2]
new_a =[]
for i in a:
    if i>5:
        i+=2
        new_a.append(i)  
print("Original arrays",a)
print("New array",new_a)