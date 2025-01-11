n=[]

a=int(input("how many numbers you want to enter: "))

for i in range(a):
    b=int(input("Enter Number: "))
    n.append(b)

print(f"max number in the list is: {max(n)}\nAnd minimum number is: {min(n)} ")

c=input("Want to see the list that you created: ").lower()

if c== 'yes':
    print(f"\nHere is your list\n{n}")
    print('\n\t#--------- Thank You ---------#')

else:
    print('\t#--------- Thank You ---------#')
