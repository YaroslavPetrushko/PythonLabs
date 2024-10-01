
import math

def expression (x):

    z=(1-2*pow(math.sin(x),2))/(1+pow(math.sin(x),2))

    return z

def product (x,y):

    dob=1

    for i in range (x,y+1):

        if i % 2 == 0:

            dob *= i

    return dob


print("Task 1. Expression.")

x=int(input('Enter x: '))

print("Result. z = ", expression(x))

print("Task 2. Product of even numbers.")

x=int(input('Enter x: '))

y=int(input('Enter y: '))

while x>y:

    x=int(input('Invalid input. y cannot be less than x, enter again. x: '))

    y=int(input('y: '))

print ("Product of even numbers from x to y = ", product(x,y))
