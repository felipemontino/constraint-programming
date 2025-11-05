from cpmpy import *

# Define variables for each letter
S, E, N, D, M, O, R, Y = intvar(0, 9, shape=8, name="letters")

model = Model([
    # All letters must be different
    AllDifferent([S, E, N, D, M, O, R, Y]),
    # Leading digits cannot be zero
    S != 0,
    M != 0,
    # SEND + MORE = MONEY
    (1000*S + 100*E + 10*N + D) +
    (1000*M + 100*O + 10*R + E) ==
    (10000*M + 1000*O + 100*N + 10*E + Y)
])

if model.solve():
    print(f"SEND = {S.value()}{E.value()}{N.value()}{D.value()}")
    print(f"MORE = {M.value()}{O.value()}{R.value()}{E.value()}")
    print(f"MONEY = {M.value()}{O.value()}{N.value()}{E.value()}{Y.value()}")
else:
    print("No solution found.")