a= int(input("enter the marks of the first subject: " ))
b= int(input("enter the marks of the second subject: " ))
c= int(input("enter the marks of the third subject: " ))

total= (100*(a+b+c))/300

# To check if the user has entered a positive number.
if (a<0 and b<0 and c<0):
    print('\tEnter a positive number')
else:
    print('\tWelcom to Grade Calculator')

# To check if the student has failed in any one subject.
if (a<33):
    print("\tYou are failed in subject 1",a)
elif (b<33):
    print("\tYou are failed in subject 2",b)
elif (c<33):
    print("\tYou are failed in subject 3",c)

# To check if the student has passed overall
if (total>=40):
    print('\tYou have been promoted\n\tAnd your precentage is:',total)
else:
    print("\tUnfortunatly you have been held back\n\tAnd your precentage is:",total)

# To claculate his grade
if(total<=100 and total>=90):
    grade='excellent'
elif(total<90 and total>=80):
    grade='A'
elif(total<80 and total>=70):
    grade='B'
elif(total<70 and total>=60):
    grade='C'
elif(total<60 and total>=50):
    grade='D'
elif(total<50 ):
    grade='Fail'

print('\tAccording to your marks you have been assigned grade:|',grade)

