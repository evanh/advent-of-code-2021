import sys

input_name = "ex.input.txt"
if "real" in sys.argv:
    input_name = "input.txt"

lines = [line.strip() for line in open(input_name, "r")]

position = 0
aim = 0
depth = 0
for line in lines:
    command, raw_amount = line.split(" ", 1)
    amount = int(raw_amount)

    if command == "forward":
        position += amount
        depth += aim * amount
    elif command == "down":
        aim += amount
    elif command == "up":
        aim -= amount

print("FINAL", position * depth)
