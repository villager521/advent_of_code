# https://adventofcode.com/2021/day/7
"""

For task 2, given a list of crabs at position x2, we need to find
a best x1 such that the cost is minimum:
- the cost of moving from x2 to x1 is: abs(x2-x1)*(abs(x2-x1)+1)/2
- the cost of moving all x2 to x1 is:
        cost = \sum_{x2 \in h_pos}abs(x2-x1)*(abs(x2-x1)+1)/2
- To find the mininum cost, let
        dcox/dx1 = \sum_{x2} (x1-x2(+-)1/2) = 0
- As x2 could be smaller or higher than x1, x1 should be between 
        [sum(x2)/n-1/2, sum(x2)/n+1/2]
where n is the total number of crabs.
- We can use int(sum(x2)/n) to approximate this best position.

"""

from pathlib import Path
from typing import List

base_path = Path(__file__).parents[0].resolve()
data_path = base_path / "input" / "input7.txt"


def load_input_data(input_file_path: str) -> List[int]:
    """Load input list from a text file."""

    file = open(input_file_path, "r")
    Lines = file.readlines()
    return [int(x) for x in Lines[0].replace("\n", "").split(",")]


def task1_align_crab(h_pos: List[int]) -> int:
    "Find the lowest fuel to align crab submarines."

    # sort the list and the middle one is the best position
    h_pos.sort()
    best_pos = h_pos[int((len(h_pos) - 1) / 2)]
    return sum([abs(best_pos - i) for i in h_pos])


def task2_align_crab(h_pos: List[int]) -> int:
    "Find the lowest fuel to align crab submarines with incremental cost."

    # get the best position
    best_pos = int(sum(h_pos) / len(h_pos))
    # get cost
    return sum([abs(x2 - best_pos) * (abs(x2 - best_pos) + 1) / 2 for x2 in h_pos])


if __name__ == "__main__":

    init_state = load_input_data(data_path)
    output1 = task1_align_crab(init_state)
    print(output1)

    output2 = task2_align_crab(init_state)
    print(output2)
