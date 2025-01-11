print( ' Welcome to the phone dirictory ')

phone_dic={}

entries=int(input('How many entries do you have to enter :'))

for i in range(entries):
    print('Hello Welcome to phone directory')

    name=input('Enter your name: ')

    number=int(input('Phone number: '))
    
    phone_dic[name]=number
print(f'\n Phone Dictionary : \n')

for name,number in phone_dic.items():
    print(f'Name: {name} ,Phone Number: {number}\n')

print(f'Do you want to continue?')

a=input('Yes or No: ')
if a == 'yes'or 'Yes':
        
    entries=int(input('How many entries do you have to enter :'))
    for i in range(entries):

        print('Hello Welcome to phone directory')

        name=input('Enter your name: ')

        number=int(input('Phone number: '))
    
        phone_dic[name]=number
        print(f'\n Phone Dictionary : \n')

    for name,number in phone_dic.items():

         print(f'Name: {name} ,Phone Number: {number}\n')


else:
    print('Thank you')
    
