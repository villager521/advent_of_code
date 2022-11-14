# https://adventofcode.com/2021/day/3
"""
Q1: what would happen if we have an equal number of zero and one?
"""
from pathlib import Path
from typing import List

base_path = Path(__file__).parents[0].resolve()
data_path = base_path / "input" / "input3.txt"


def text_to_array(input_file_path: str) -> List[List[int]]:
    """Load input text as a 2d list of integer."""

    report = []
    # Read input data
    file = open(input_file_path, "r")
    Lines = file.readlines()
    for line in Lines:
        if not report:
            # Initialise
            len_record = len(line.replace("\n", ""))
            report = [[int(line[i])] for i in range(len_record)]
        # Update lists of columns
        for i in range(len_record):
            report[i].append(int(line[i]))

    return report


def get_common_digit(input: List[int]) -> int:
    """Get the most column bit in a list."""
    return int(sum(input) >= len(input) / 2)


def binary_to_decimal(input: List[int]) -> int:
    """Convert a list of bits into a decimal number."""
    l = len(input)
    return sum([2 ** (l - i - 1) * input[i] for i in range(l)])


def get_rating(report: List[List[int]], type_name: str) -> int:
    """Get the oxygen generator or co2 rating."""

    i, l_report = 0, len(report[0])
    ind = list(range(l_report))
    # Loop through each column of bits until one item left
    while (i < l_report) and (len(ind) > 1):
        # Get the latest column
        col = [report[i][x] for x in ind]
        # Get the most common digit
        max_digit = get_common_digit(col)
        if type_name == "co2":
            max_digit = 1 - max_digit
        # Get the global index of the digits to keep
        ind = [ind[j] for j, y in enumerate(col) if y == max_digit]
        i += 1

    return binary_to_decimal([x[ind[0]] for x in report])


def task1_get_power_consumption(input_file_path: str):
    """get the power consumption of the submarine."""

    report = text_to_array(input_file_path)
    # Get the most common digits
    max_digits = [get_common_digit(x) for x in report]

    # Convert the binary number to a decimal number
    gamma_rate = binary_to_decimal(max_digits)

    # Convert the list of least common bitsto a decimal number
    epsilon_rate = binary_to_decimal([1 - x for x in max_digits])

    return gamma_rate * epsilon_rate


def task2_verify_life_support(input_file_path: str):
    """verify the life support rating based on oxygen and CO2."""

    report = text_to_array(input_file_path)
    # Get two ratings
    oxygen_rating = get_rating(report, "oxygen")
    co2_rating = get_rating(report, "co2")

    return oxygen_rating * co2_rating


if __name__ == "__main__":

    output1 = task1_get_power_consumption(data_path)
    print(output1)

    output2 = task2_verify_life_support(data_path)
    print(output2)
