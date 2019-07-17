NumberStr = ['零','一','二','三','四','五','六','七','八','九']
number = input('')
for i in number:
    a = eval(i)
    #print(i)
    print(NumberStr[a],end='')
