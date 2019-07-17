C = int(input())
a = 0          #两个字符后输出换行
str = "Hello World"
if (C == 0):
    print(str)
elif (C > 0):
    for i in str:
        print(i,end='')
        a=a+1
        if (a%2 == 0):
            print()
else:
    for i in str:
        print(i)
    
