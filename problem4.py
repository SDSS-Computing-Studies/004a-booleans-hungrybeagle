#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# It is close enough if the expected length of the hypotenuse and the actual length 
# differ by no more than 2% 
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"
import math
 
n1 = float(input ("enter a side:"))
n2 = float(input ("enter a side:"))
n3 = float(input ("enter a side:"))
nums = (n1, n2, n3)
c = max(nums)
a = min(nums)
b = n1 + n2 + n3 - a - c

hyp = math.sqrt(a**2 + b**2)

if c  > hyp*1.02:
    print("that is an obtuse triangle")
elif c < hyp * 0.98:
    print("that is an acute triangle")
else:
    print("that is a right triangle")