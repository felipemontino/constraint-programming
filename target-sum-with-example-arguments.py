from cpmpy import *

# The domain argument allows you to specify the range of values that the variables (x and y) can take. In constraint programming, variables often have domains that restrict their possible values. By passing domain as a parameter, you make the function flexible and reusable for different ranges, rather than hardcoding the variable bounds.
# For example, domain=(0, 10) means x and y can take any integer value from 0 to 10. If you want to solve a similar problem with a different range, you can simply change the domain argument.
# This approach demonstrates how constraint programming models can be parameterized, making them adaptable to different scenarios or user inputs. If you have a specific use case, you can pass relevant parameters (like domain, target sum, constraints, etc.) to your model-building function.
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