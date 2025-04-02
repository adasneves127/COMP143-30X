
# Libraries and Packages

# Math Library
# Random Library
# Datetime Library

import math

print(math.floor(4.999999))


import random

print(random.randint(0, 10))
my_list = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(my_list)
print(my_list)

import datetime
now = datetime.datetime.now()
print((now + datetime.timedelta(31)).strftime("%b %d, %Y %H:%m:%S"))
print(datetime.datetime.strptime("May 01, 2025 09:01:22", "%b %d, %Y %H:%m:%S"))
