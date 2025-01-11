l=['harry','jack','oggy','taufiq']

user=input('enter your name: ')
if (len(user)<=3):
    print('Please enter a valid name')
elif(user.lower() in l):
    print(f'congratulations, you have been selected {user.upper()}!')
else:
    print('sorry you have not been selected\nPlease try next year.')