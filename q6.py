#find the second largest number among the three inputs given.
a=int(input('enter input'))
b=int(input('enter number'))
c=int(input('enter number'))
if a>c and a<b:
    print('a is second largest')
elif a>b and b<c:
    print(' c is second largest')
elif c<b and a>b:
    print('b is second largest')
else:
    print('no second largest')