in_number = input("")
if in_number[-3:] in ['USD','usd']:
    RMB = eval(in_number[0:-3]) * 6.78
    print("RMB{:.2f}".format(RMB))
elif in_number[-3:] in ['RMB','rmb']:
    USD = eval(in_number[0:-3]) / 6.78
    print("USD{:.2f}".format(USD))
