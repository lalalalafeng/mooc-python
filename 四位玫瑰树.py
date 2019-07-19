for i in range(1000,10000):
    qianwei = i//1000
    baiwei  = i%1000//100
    shiwei  = i%100//10
    gewei   = i%10
    result = pow(qianwei,4)+ pow(baiwei,4)+pow(shiwei,4)+pow(gewei,4)
    if i == result:
        print(i)
