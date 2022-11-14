# https://adventofcode.com/2021/day/8
"""
For task 2, consider the difference between different numbers:
- number 0: abc efg             | 6, cf,~bd
- number 1:   c  f  | len(x) = 2
- number 2: a cde g                         | 5
- number 3: a cd fg                         | 5, cf
- number 4:  bcd f  | len(x) = 4
- number 5: ab d fg                         | 5, bd
- number 6: ab defg             | 6
- number 7: a c  f  | len(x) = 3
- number 8: abcdefg | len(x) = 7
- number 9: abcd fg             | 6, cf, bd
=>
  - number 1:'cf'
  - set_diff(4, 1): 'bd'
"""
from pathlib import Path
from typing import List, Dict

base_path = Path(__file__).parents[0].resolve()
data_path = base_path / "input" / "input8.txt"


def task1_count_digits(input_file_path: str) -> int:
    """Count the occurrence of 1, 4, 7, 8."""

    digits_count = 0
    # Load input file
    file = open(input_file_path, "r")
    Lines = file.readlines()
    for line in Lines:
        digits = line.replace("\n", "").split(" | ")[1].split(" ")
        for x in digits:
            if len(x) in [2, 3, 4, 7]:
                digits_count += 1

    return digits_count


def str_in_another(str1: str, str2: str) -> bool:
    """Check if all characters in str1 are in str2."""
    return all([x in str2 for x in str1])


def decode_input(input: str) -> Dict:
    "Map an input list of strings to corresponding digits."

    mapping = {}
    # Map from segment length to digit
    len_to_digit = {2: 1, 3: 7, 4: 4, 7: 8}

    # Sort input list by length of strings
    input = sorted(input, key=len)
    for i, x in enumerate(input):
        # Sort each string
        x = "".join(sorted(x))
        if i <= 2 or i == 9:
            mapping[x] = len_to_digit[len(x)]
            if i == 0:
                cf = x
            elif i == 2:
                bd = "".join(set(x) - set(cf))
        else:
            # Check 2, 3, 5
            if len(x) == 5:
                if str_in_another(cf, x):
                    mapping[x] = 3
                elif str_in_another(bd, x):
                    mapping[x] = 5
                else:
                    mapping[x] = 2
        # Check 0, 6, 9
        if len(x) == 6:
            if str_in_another(cf, x):
                if str_in_another(bd, x):
                    mapping[x] = 9
                else:
                    mapping[x] = 0
            else:
                mapping[x] = 6
    return mapping


def get_output(output: List[str], mapping: Dict) -> int:
    "Map a list of strings into number using the decoded mapping."
    return sum(
        [10 ** (3 - i) * mapping["".join(sorted(x))] for i, x in enumerate(output)]
    )


def task2_sum_output(input_file_path: str) -> int:
    "Get the sum of all output values in the input file."

    # load input file
    file = open(input_file_path, "r")
    Lines = file.readlines()
    final_value = 0
    for line in Lines:
        digits = line.replace("\n", "").split(" | ")
        mapping = decode_input(digits[0].split(" "))
        final_value += get_output(digits[1].split(" "), mapping)

    return final_value


if __name__ == "__main__":

    output1 = task1_count_digits(data_path)
    print(output1)

    output2 = task2_sum_output(data_path)
    print(output2)
