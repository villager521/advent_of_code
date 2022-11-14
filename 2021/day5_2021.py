# https://adventofcode.com/2021/day/5

from pathlib import Path
from typing import List, Dict

base_path = Path(__file__).parents[0].resolve()
data_path = base_path / "input" / "input5.txt"


def get_overlapping_points(points: List[int], task_name: str = "task1"):
    """Get the points between two input points."""

    x = [points[0], points[2]]
    y = [points[1], points[3]]
    # Get points when the input line is vertical
    if x[0] == x[1]:
        y.sort()
        y_all = range(y[0], y[1] + 1)
        x_all = [x[0]] * (y[1] - y[0] + 1)
    else:
        # Otherwise, get the slope of the line
        a = (y[0] - y[1]) / (x[0] - x[1])
        if (
            ((a != 0) and (task_name == "task1"))
            or (abs(a) not in [0, 1])
            and (task_name == "task2")
        ):
            # Skip a line if it is not horizontal for task 1,
            # or not horizontal or diagonal for task 2
            return [], []
        # Otherwise, get all overlapping points in between
        b = y[0] - a * x[0]
        x.sort()
        x_all = range(x[0], x[1] + 1)
        y_all = [a * x0 + b for x0 in x_all]

    return x_all, y_all


def update_diagram(x_all: List[int], y_all: List[int], output: Dict):
    """Update the occurrence of points in the diagram."""

    # Loop through all points to update the diagram
    for x0, y0 in zip(x_all, y_all):
        # Use postion as the key of the output dict
        key = tuple([x0, y0])
        if key in output:
            output[key] += 1
        else:
            output[key] = 1
    return output


def task_load_vents_data(input_file_path: str, task_name: str = "task1") -> int:
    """Read input file and return the number of satisfying points."""

    # Initialise the output diagram as a dictionary
    output = {}
    # Load input data
    file = open(input_file_path, "r")
    Lines = file.readlines()
    for line in Lines:
        points = [int(x) for x in line.replace(" -> ", ",").split(",")]
        x_all, y_all = get_overlapping_points(points, task_name)
        output = update_diagram(x_all, y_all, output)

    # Check number of points >= 2
    return len([key for key, value in output.items() if value >= 2])


if __name__ == "__main__":

    output1 = task_load_vents_data(data_path, task_name="task1")
    print(output1)

    output2 = task_load_vents_data(data_path, task_name="task2")
    print(output2)
  
