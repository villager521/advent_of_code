# https://adventofcode.com/2021/day/6

from pathlib import Path
from typing import List

base_path = Path(__file__).parents[0].resolve()
data_path = base_path / "input" / "input6.txt"


def load_input_data(input_file_path: str) -> List[int]:
    """Load input list from a text file."""

    # Load input data
    file = open(input_file_path, "r")
    Lines = file.readlines()
    # Return the first line
    return [int(x) for x in Lines[0].replace("\n", "").split(",")]


def task1_count_lanternfish(state: List[int], n_days: int) -> int:
    "Count the number of lantern fish after n_days."

    n = 0
    while n < n_days:
        new_fish = []
        for i, x in enumerate(state):
            if x == 0:
                state[i] = 6
                new_fish.append(8)
            else:
                state[i] -= 1
        state += new_fish
        n += 1

    return len(state)


def task2_count_lanternfish(state: List[int], n_days: int) -> int:
    "Count the number of fish using another method."

    num_fish = len(state)
    for x in state:
        fish = [0] * n_days
        fish[x] = 1
        for i in range(n_days):
            # follwoing generations
            if fish[i - 9] != 0:
                fish[i] += fish[i - 9]
            if fish[i - 7] != 0:
                fish[i] += fish[i - 7]
        num_fish += sum(fish)
    return num_fish


if __name__ == "__main__":

    #init_state = load_input_data(data_path)
    #output1 = task1_count_lanternfish(init_state, 256)
    #print(output1)

    init_state = load_input_data(data_path)
    output2 = task2_count_lanternfish(init_state, 256)
    print(output2)


# def task2_count_lanternfish(state: List[int], n_days: int) -> int:
#     "Count the number of fish using another method."

#     num_fish = len(state)

#     for x in state:
#         # first generation
#         x1 = list(range(x, n_days, 7))
#         # following generations are created every nine days
#         while len(x1) > 0:
#             num_fish += len(x1)
#             # break if no new fish will be born
#             if x1[0] > n_days-9:
#                 break
#             x2 = []
#             for x0 in x1:
#                 x2 += (list(range(x0+9, n_days, 7)))
#             x1 = x2
#     return num_fish
