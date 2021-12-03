import sys

input_name = "ex.input.txt"
if "real" in sys.argv:
    input_name = "input.txt"

lines = [line.strip() for line in open(input_name, "r")]

prev = None
count = 0
for line in lines:
    cur = int(line)
    if prev is None:
        prev = cur
        continue

    if cur > prev:
        count += 1

    prev = cur

print("COUNT", count)
