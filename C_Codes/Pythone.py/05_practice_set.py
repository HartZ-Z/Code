print('       Welcome to the Diary        ')

d={}

n=int(input('How many entries you want to enter: '))

for i in range (n):
    a=input('Hello entre your name : ')
    b=input('Now enter your fav coding language : ')
    d[a]=(b)
for a,b in d.items():
    print(a,b)

x=input('Do you want to continue : ')

if x== 'yes' or "Yes":
    p=int(input('How many entries you want to enter: '))

for i in range (p):
    a=input('Hello entre your name : ')
    b=input('Now enter your fav coding language : ')

    d[a]=(b)
    
    for a,b in d.items():
        print(f"Name:{a} Language:{b}")

    print(d)
else:
    print("     Thank you :)     ")    
