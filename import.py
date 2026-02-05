# Practicing import in Python

# importing full module
import math

num = 12
result = math.sqrt(num) * math.pi
print("Using full math module:", result)


# importing specific things
from math import sqrt, pi

result2 = sqrt(12) * pi
print("Using specific import:", result2)


# importing from custom file
from rough_work import rohan, handsome

rohan()
print("Value from custom file:", handsome)
