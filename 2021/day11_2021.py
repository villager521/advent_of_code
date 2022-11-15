# https://adventofcode.com/2021/day/10
"""
Note as the numpy array is changed in task 1, 
need to re-initialise it when used in task 2.
"""

from pathlib import Path
import numpy as np


base_path = Path(__file__).parents[0].resolve()
data_path = base_path / "input" / "input11.txt"


def load_input(input_file_path: str) -> np.array:
    "Load the input data as a numpy array."

    output = []
    file = open(input_file_path, "r")
    Lines = file.readlines()
    for line in Lines:
        output.append([int(i) for i in line.replace("\n", "")])
    # Add zero padding around the input array
    output = np.pad(np.array(output), (1, 1), "constant", constant_values=(-2, -2))
    return output


def update_energy_level(
    input: np.array,
    i: int,
    j: int,
):
    "Update the energy at (i,j) and its 8-nearby locations."

    # Return at boundary or already flashed elements
    if input[i, j] == -2 or input[i, j] == -1:
        return
    # Otherwise, increse by 1
    input[i, j] += 1
    # Flashing
    if input[i, j] > 9:
        input[i, j] = -1
        update_energy_level(input, i, j - 1)
        update_energy_level(input, i, j + 1)
        update_energy_level(input, i - 1, j - 1)
        update_energy_level(input, i - 1, j)
        update_energy_level(input, i - 1, j + 1)
        update_energy_level(input, i + 1, j - 1)
        update_energy_level(input, i + 1, j)
        update_energy_level(input, i + 1, j + 1)


def task1_number_flashes(input: np.array, k: int) -> int:
    "Get the number of flashes after step k, O(kmn)."

    rows, cols = input.shape[0], input.shape[1]
    n_flash = 0
    for step in range(k):
        for i in range(rows):
            for j in range(cols):
                update_energy_level(input, i, j)

        # Count flashed elements
        n_flash += sum(sum(input == -1))
        # Replace all flashed element as 0
        np.place(input, input == -1, [0])

    return n_flash


def task2_find_simultaneous_flashing(input: np.array) -> int:
    "Find the first time when all elements flash simultaneously."

    rows, cols = input.shape[0], input.shape[1]
    step = 0
    while True:
        step += 1
        for i in range(rows):
            for j in range(cols):
                update_energy_level(input, i, j)
        # Return if all flashed
        if np.all(input[1:-1, 1:-1] == -1):
            return step
        # Replace all flashed element as 0
        np.place(input, input == -1, [0])


if __name__ == "__main__":

    input = load_input(data_path)
    output1 = task1_number_flashes(input, 100)
    print(output1)

    input = load_input(data_path)
    output2 = task2_find_simultaneous_flashing(input)
    print(output2)
