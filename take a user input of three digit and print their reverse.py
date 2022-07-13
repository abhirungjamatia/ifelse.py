num=int(input('enter number'))
if num>99 and num<1000:
    a=num//10
    b=num%10
    c=a%10
    d=a//10
    b=str(b)
    c=str(c)
    d=str(d)
    print(b+c+d)