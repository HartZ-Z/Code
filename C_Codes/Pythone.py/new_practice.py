x=int(input('Enter your number : '))
y=int(input('Enter your number : '))
z=int(input('Enter your number : '))
a=int(input('Enter your number : '))

if (x>y and x>z and x>a):
    print(f'{x} is the greast number ')
elif (y>x and y>z and y>a):
    print(f'{y} is the greates number ')    
elif (z>x and z>y and z>a):
    print(f'{z} is the greates number ')    
elif (a>x and a>z and a>y):
    print(f'{a} is the greates number ')    