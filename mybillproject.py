
sum=0
while(True):
    userinput=input('Enter the item price or enter  N to quit')
    if (userinput!="N"):
        sum=sum+int(userinput)
        print(f'your total is :{sum}')
    else:
        print(f'your total bill is {sum}, thanks for shopping with us')
        break 
