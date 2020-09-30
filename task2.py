#! python3
# Have the user input a number 
# Determine if the number is positive, negative or 0 
# 2 points

# Inputs:
# number

# Outputs:
# - "positive"
# - "negative"
# - "zero"

a = float( input("number:"))
if a > 0:
    print('positive')
elif a < 0:
    print("negative")
else:
    print("zero")