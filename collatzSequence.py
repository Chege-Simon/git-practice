#! /usr/bin/python3

print("Enter number:")
number = 0
def collatz(number):
    while number > 1:
            if number % 2 == 0:
                number = number // 2
                print(number)

            elif number % 2 == 1:
                number = 3 * number + 1
                print(number)
                
    number = number
       

 
try:
    number = int(input())
except ValueError:
            print("Please enter an integer")
            
collatz(number)
