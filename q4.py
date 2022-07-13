#take an user input and check the following:
#_if its divisible by 3 print ice,if its divisible by 9 print cream and if its divisible by both print ice cream.
a=int(input('enter number'))
if a%3==0:
    print('ice')
elif a%9==0:
    print('cream')
elif a%3==0 and a%9==0:
    print('ice cream')
else:
    print('none')
