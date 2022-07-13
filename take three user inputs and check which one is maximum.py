a=int(input('enter number'))
b=int(input('enter number'))
c=int(input('enter number'))
if a>b and a>c:
    print('a is maximum')
elif b>a and b>c:
    print('b is maximum')
elif c>a and c>b:
    print('c is maximum')
else:
    print('none')