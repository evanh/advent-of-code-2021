import sys
from math import ceil, floor

input_name = "ex.input.txt"
if "real" in sys.argv:
    input_name = "input.txt"

readings = sorted([line.strip() for line in open(input_name, "r")])

def most_common_binary_search(digits, idx):
    if len(digits) == 1:
        return digits[0]

    middle = floor(len(digits) / 2.0)
    most_common = digits[middle][idx]
    if most_common == "1":
        most_left = middle
        while most_left != 0 and digits[most_left][idx] == most_common:
            most_left -= 1

        return most_common_binary_search(digits[most_left+1:], idx+1)
    else:
        most_right = middle
        max_val = len(digits) - 1
        while most_right != max_val and digits[most_right][idx] == most_common:
            most_right += 1

        return most_common_binary_search(digits[:most_right], idx+1)


def least_common_binary_search(digits, idx):
    if len(digits) == 1:
        return digits[0]

    if len(digits) % 2 == 1:
        middle = floor(len(digits) / 2.0)
        least_common = "0" if digits[middle][idx] == "1" else "1"
    else:
        middle = floor(len(digits) / 2.0)
        left, right = digits[middle-1], digits[middle]
        if left[idx] != right[idx]:
            least_common = "0"
        else:
            least_common = "0" if right[idx] == "1" else "1"

    if least_common == "1":
        most_right = middle
        max_val = len(digits) - 1
        while most_right != max_val and digits[most_right][idx] != least_common:
            most_right += 1

        return least_common_binary_search(digits[most_right:], idx+1)
    else:
        most_left = middle
        while most_left != 0 and digits[most_left][idx] != least_common:
            most_left -= 1

        return least_common_binary_search(digits[:most_left+1], idx+1)


most_common = most_common_binary_search(readings, 0)
least_common = least_common_binary_search(readings, 0)

oxygen = int(most_common, 2)
co2 = int(least_common, 2)

print(f"{oxygen} O x {co2} C = {oxygen * co2}")




# # least common
# ['00010', '00100', '00111', '01010', '01111', '10000', '10101', '10110', '10111', '11001', '11100', '11110']



# # most common
# ['00010', '00100', '00111', '01010', '01111', '10000', '10101', '10110', '10111', '11001', '11100', '11110']

# ['10000', '10101', '10110', '10111', '11001', '11100', '11110']

# ['10000', '10101', '10110', '10111']

# '10101', '10110', '10111']

# '10110', '10111']

# '10111']