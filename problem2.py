#! python3

# Have the user enter a number 
# Determine if the number is an integer
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is an integer"
# "the number is not an integer"

x = input("enter a number ")
x = float(x)

if x == round(x,0):
    print(f"{x} is an integer")
else:
    print(f"{x} is not an integer")