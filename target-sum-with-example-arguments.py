from cpmpy import *

def solve_sum_problem(target_sum, domain):
    # Receive parameters from outside
    x = intvar(domain[0], domain[1], name="x")
    y = intvar(domain[0], domain[1], name="y")
    model = Model([x + y == target_sum])
    if model.solve():
        print(f"x = {x.value()}, y = {y.value()}")
    else:
        print("No solution found.")

# Example usage with parameters
solve_sum_problem(15, (0, 10))