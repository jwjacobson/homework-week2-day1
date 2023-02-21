#! /usr/bin/python

# Exercise #1
# Print out all cubed numbers up to the total value 1000.

list_num = []
total = 0
x = 0

print("Cubes from 0 to 100:")
while total < 1000:
    list_num.append(x**3)
    total = x ** 3
    x += 1
[print(num) for num in list_num]

# Exercise #2
# Get first prime numbers up to 100
def isprime(x):
    if x <= 1:
        return False
    elif x == 2:                 # my approach takes as axiomatic that 2 is the first prime
        return True
    else:
        for num in range(2, x):
            if x % num == 0:
                return False
        else:
            return True

print("\nPrimes up to 100:")
for num in range(0, 101):
    if isprime(num):
        print(num)


# Exercise 3
# Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors

x = input("\nHow old are you? ")
if x.isdigit():                 # Checking that x is a digit prevents any weird input from crashing the program (I think)
    x = int(x)
    if x < 18:
        print("\nkids")
    elif x <= 65:
        print("\nadults")
    else:
        print("\nseniors")
else:
    print("\ninvalid input (must be positive integer)")