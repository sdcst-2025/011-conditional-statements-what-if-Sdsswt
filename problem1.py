#! python3

# Have the user enter a number 
# Determine if the number is an even number. 
# There are many ways to solve this problem
# Hint: One method is to use the modulus, which determines the remainder when two numbers are divided
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is even"
# "the number is odd"
x = input("enter a number ")
x = int(x)

if x % 2 == 0:
    print(f"{x} is even")
else:
    print(f"{x} is odd")