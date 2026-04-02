# Cryptarithm Solver 

import itertools

def solve_cryptarithm():
    letters = "SENDMORY"
    digits = range(10)

    for perm in itertools.permutations(digits, len(letters)):
        assign = dict(zip(letters, perm))

        # Leading digits cannot be zero
        if assign['S'] == 0 or assign['M'] == 0:
            continue

        # Form numbers
        SEND = 1000*assign['S'] + 100*assign['E'] + 10*assign['N'] + assign['D']
        MORE = 1000*assign['M'] + 100*assign['O'] + 10*assign['R'] + assign['E']
        MONEY = 10000*assign['M'] + 1000*assign['O'] + 100*assign['N'] + 10*assign['E'] + assign['Y']

        if SEND + MORE == MONEY:
            print("\nSolution Found!\n")
            print("Mapping:", assign)
            print(f"\nSEND  = {SEND}")
            print(f"MORE  = {MORE}")
            print(f"MONEY = {MONEY}")
            return

    print("No solution found")


if __name__ == "__main__":
    solve_cryptarithm()
