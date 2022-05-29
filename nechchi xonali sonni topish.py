a=int (input('a='))
b=a
xonalar_soni=0
while b!=0:
    b=b//10
    xonalar_soni+=1
if a==0:
    print('nol soni keritildi')
else:
    if a%2==1:
        print(f' {xonalar_soni}xonali toq son')
    elif a%2==0:
        print(f' {xonalar_soni} xonali juft son')
    '''if a<0 and a%2==1:
        print('manfiy toq son')
    elif a<0 and a%2==0:
        print('manfiy juft son')'''
