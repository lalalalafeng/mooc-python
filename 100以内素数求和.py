total = 0
for i in range(2,100):
    a = 2
    for a in range(2,i):
        if i%a == 0:
            break
    else:
        total +=i
print(total)
