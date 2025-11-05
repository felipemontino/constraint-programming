from cpmpy import *
import numpy as np

# Define variables
x = intvar(0, 10, name="x")
y = intvar(0, 10, name="y")

# Define constraints
model = Model([
    x + y == 10,
    x > y
])

# Solve the model
if model.solve():
    print(f"x = {x.value()}, y = {y.value()}")
else:
    print("No solution found.")