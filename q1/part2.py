import sys
import os

input_name = "ex.input.txt"
if "real" in sys.argv:
    input_name = "input.txt"

lines = [line.strip() for line in open(input_name, "r")]

first, second, third = None, None, None
sums = []
for line in lines:
    cur = int(line)
    if first is None:
        first = [cur]
        continue

    if len(first) == 3:
        sums.append(sum(first))
        first = second
        second = third
        third = None

    first.append(cur)

    if second is None:
        second = [cur]
        continue

    second.append(cur)

    if third is None:
        third = [cur]
        continue

    third.append(cur)

sums.append(sum(first))

prev = None
count = 0
for agg in sums:
    if prev is None:
        prev = agg
        continue

    if agg > prev:
        count += 1

    prev = agg

print(count)