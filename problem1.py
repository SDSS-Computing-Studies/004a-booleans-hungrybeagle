#! python3

# Have the user enter a number 
# Determine if the number is an even number. 
# Hint: Use the modulus, which determines the remainder when two numbers are divided
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is even"
# "the number is odd"

num = input("Enter a positive integer")
if num%2 ==0 :
    print('the numbers is even')
else:
    print("the number is odd")