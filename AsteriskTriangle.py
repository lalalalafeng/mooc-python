#AsteriskTriangle.py
N = eval(input())
for i in range(1, N+1, 2):
   print("{0:^{1}}".format('*'*i, N))
