#Написати програму, яка обчислює значення X в залежності 
#від значень a та b, введених користувачем з клавіатури

a=int(input('Enter a: '))

while (a<1 or a>100):

    a=int(input("Invalid input. Try again. a:"))

b=int(input('Enter b: '))

while (b<1 or b>100):

    b=int(input("Invalid input. Try again. b:"))

if a<b:

    x=b/a+1

elif a==b: 

    x=25

else:

    x=(a^3-5)/b

print("Result: ", x)



