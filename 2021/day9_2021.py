# https://adventofcode.com/2021/day/9
"""
for task 1, in order to find all local minimum in a 2D array, it seems we need 
to loop through all elements so O(n^2) would be the best solution? Binary search
/Divide-and-Conquer method can only return one local minima...

for task 2, it would be good to use a seed growing approach to find all 
elements belonging to the same cluster, then move to a following cluster.
Tried to avoid looping through all elements but not sure how to guarantee
all elements are visited. Had a look of online solutions....
"""

from pathlib import Path
from typing import List
import numpy as np


base_path = Path(__file__).parents[0].resolve()
data_path = base_path / "input" / "input9.txt"


def load_input(input_file_path: str) -> np.array:
    "Load the input data as a numpy array."

    output = []
    file = open(input_file_path, "r")
    Lines = file.readlines()
    for line in Lines:
        output.append([int(i) for i in line.replace("\n", "")])

    return np.array(output)


def task1_get_local_minimum(input: np.array) -> int:
    "Get the sum of local minum in a 2-D array."

    # Add zero padding around the input array
    input = np.pad(input, (1, 1), "constant", constant_values=(10, 10))
    rows, cols = input.shape[0], input.shape[1]
    local_minima = 0
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if (
                input[i, j] < input[i, j + 1]
                and input[i, j] < input[i, j - 1]
                and input[i, j] < input[i - 1, j]
                and input[i, j] < input[i + 1, j]
            ):
                local_minima += 1 + input[i, j]

    return local_minima


def search_cluster(input: np.array, i: int, j: int, cluster: List[int]):
    """Find the number of connected points in a cluster."""

    # Return when reaching the boundary, or 9, or a previously visited element
    if (
        i < 0
        or i == input.shape[0]
        or j < 0
        or j == input.shape[1]
        or input[i, j] == 9
        or input[i, j] == -1
    ):
        return
    # Add one element into the latest cluster
    cluster[-1] += 1
    # Update visited element as -1
    input[i, j] = -1
    # Search right, bottom, left, and top element
    search_cluster(input, i, j + 1, cluster)
    search_cluster(input, i + 1, j, cluster)
    search_cluster(input, i, j - 1, cluster)
    search_cluster(input, i - 1, j, cluster)


def task2_sum_basin(input: np.array) -> int:
    """Get the sum of the three largest basin."""

    rows, cols = input.shape[0], input.shape[1]
    cluster = []
    for i in range(0, rows):
        for j in range(0, cols):
            if input[i, j] != -1:
                cluster.append(0)
                search_cluster(input, i, j, cluster)

    cluster.sort(reverse=True)
    # print("-----\n", cluster)
    return cluster[0] * cluster[1] * cluster[2]


if __name__ == "__main__":

    input = load_input(data_path)
    output1 = task1_get_local_minimum(input)
    print(output1)

    output2 = task2_sum_basin(input)
    print(output2)
