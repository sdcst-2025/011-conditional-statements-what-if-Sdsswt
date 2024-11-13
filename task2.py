#! python3
"""
 Have the user input a number 
 Determine if the number is positive, negative or 0 
 2 points

 Inputs:
 number

 Outputs:
 - "positive"
 - "negative"
 - "zero"

 Example:

Enter a number: 3
positive

Enter a number: -1.2
negative
"""

a = input("Enter a number ")
a = int(a)

if a >= 1:
    print(f"{a} is positive")

if a < 0:
    print(f"{a} is negative")

if a == 0:
    print(f"{a} is equel to 0")