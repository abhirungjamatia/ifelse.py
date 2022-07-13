#write a python program to check the given number:
#if n is even and in the inclusive range of 2-5 print not weird
#if n is even and in the inclusive range of 6-20 print weird,if n is odd and greaterthan 30 print not weird.
n=int(input('enter number'))
if n%2==0 and n>=6 and n<=20:
    print('weird')
elif n%2==0 and n>=2 and n<=5:
    print('not weird')
elif n%2!=0 and n>30:
    print('not weird')
else:
    print('none')

