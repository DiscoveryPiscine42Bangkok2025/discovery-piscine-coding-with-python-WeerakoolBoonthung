a = [2, 8, 9, 48, 8, 22, -12, 2]
new_a = []
for i in a:
    if a.count(i) == 1:
        new_a.append(i+2)
print(a)
print(new_a)