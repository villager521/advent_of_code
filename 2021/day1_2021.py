# https://adventofcode.com/2021/day/1
from pathlib import Path
from typing import List


base_path = Path(__file__).parents[0].resolve()
data_path = base_path / "input" / "input1.txt"


def text_to_list(input_file_path: str) -> List[int]:
    """Convert the input text into a list of integer."""

    output = []
    # Load input data from a text file
    file = open(input_file_path, "r")
    Lines = file.readlines()
    for line in Lines:
        output.append(int(line))
    return output


def task1_count_depth_increase(input: List[int]) -> int:
    """Count the number of times a depth measurement increases from the previous one."""

    num_measures = len(input)
    if num_measures < 2:
        return 0
    else:
        return sum([input[i] > input[i - 1] for i in range(1, num_measures)])


def task2_count_window_increase(input: List[int]) -> int:
    """Count the number of times the sum of three measurements in a sliding window increases from the previous sum."""

    num_measures = len(input)
    if num_measures <= 3:
        return 0
    else:
        sum_window = [sum(input[i : i + 3]) for i in range(0, num_measures - 2)]
        return task1_count_depth_increase(sum_window)


if __name__ == "__main__":

    output1 = task1_count_depth_increase(text_to_list(data_path))
    print(output1)

    output2 = task2_count_window_increase(text_to_list(data_path))
    print(output2)
