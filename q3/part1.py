import sys

input_name = "ex.input.txt"
if "real" in sys.argv:
    input_name = "input.txt"

lines = [line.strip() for line in open(input_name, "r")]


positions = None
for line in lines:
    digits = list(line)
    if positions is None:
        positions = [{} for x in range(len(digits))]

    for i, digit in enumerate(digits):
        positions[i][digit] = positions[i].get(digit, 0) + 1

gamma_digits = []
epsilon_digits = []
for p in positions:
    if p["1"] > p["0"]:
        gamma_digits.append("1")
        epsilon_digits.append("0")
    else:
        gamma_digits.append("0")
        epsilon_digits.append("1")

gamma = int("".join(gamma_digits), 2)
epsilon = int("".join(epsilon_digits), 2)

print(f"{gamma} G x {epsilon} E = {gamma * epsilon}")