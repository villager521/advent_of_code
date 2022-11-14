# https://adventofcode.com/2021/day/4
"""
Q1: what would happen if we have the equal number of zero and one?
    which data structure is the best for this problem?
"""
from pathlib import Path
from typing import List, Union
import numpy as np


base_path = Path(__file__).parents[0].resolve()
data_path = base_path / "input" / "input4.txt"


def load_bingo_data(input_file_path: str):
    """Read an input file and return selected numbers and boards."""

    numbers, boards = [], []
    # Load input data
    file = open(input_file_path, "r")
    Lines = file.readlines()
    for line in Lines:
        if not numbers:
            # Save selected numbers
            numbers = [int(x) for x in line.split(",")]
        elif line == "\n":
            # Start a new board
            boards.append([])
        else:
            # Update board information on each row
            boards[-1].append([(int(line[i : i + 2])) for i in range(0, 15, 3)])

    return numbers, np.array(boards)


def get_winning_board(input_file_path: str, type_name: str = "first") -> int:
    """Get the final score of the first winning board."""

    numbers, boards = load_bingo_data(input_file_path)
    x, y, z = np.shape(boards)
    # Initialise the score of each board as -1
    final_score = [-1] * x

    for val in numbers:
        # Mark a board position as -1 if the number was identified
        boards[np.where(boards == val)] = -1
        # Check numbers in each row and column
        for i in range(x):
            for j in range(y):
                for k in range(z):
                    if np.all(boards[i, j, :] == -1) or np.all(boards[i, :, k] == -1):
                        # Calculate the final score of a board
                        final_score[i] = val * sum(boards[i][boards[i] != -1])
                        # Stop when one board won (task 1) or all boards have won (task 2)
                        if (type_name == "first") or (
                            sum([score != -1 for score in final_score]) == x
                        ):
                            return final_score[i]


if __name__ == "__main__":

    output1 = get_winning_board(data_path, type_name="first")
    print(output1)

    output2 = get_winning_board(data_path, type_name="last")
    print(output2)
