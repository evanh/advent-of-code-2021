import sys

question = __file__.strip(".py")
input_name = ".ex.input"
if "real" in sys.argv:
    input_name = ".input"

lines = [line.strip() for line in open(f"{question}{input_name}", "r")]

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
