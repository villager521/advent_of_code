# https://adventofcode.com/2021/day/2
from pathlib import Path

base_path = Path(__file__).parents[0].resolve()
data_path = base_path / "input" / "input2.txt"


def task1_get_planned_course(input_file_path: str) -> int:
    """get the horizontal position and depth based on planned course."""

    # Pose initialisation
    h_pos, depth = 0, 0
    # Set multiplier of planned movements
    planned_course = {"forward": 1, "down": 1, "up": -1}

    # Load input data
    file = open(input_file_path, "r")
    Lines = file.readlines()
    for line in Lines:
        dir, units = line.split(" ")
        move = planned_course[dir] * int(units)
        if dir == "forward":
            h_pos += move
        else:
            depth += move

    return h_pos * depth


def task2_get_course_with_aim(input_file_path: str) -> int:
    """get the horizontal position and depth based on planned course with aims."""

    # Pose initialisation
    aim, h_pos, depth = 0, 0, 0
    # Set multiplier of planned movements
    planned_course = {"down": 1, "up": -1}

    # Load input data
    file = open(input_file_path, "r")
    Lines = file.readlines()
    for line in Lines:
        dir, units = line.split(" ")
        if dir == "forward":
            h_pos += int(units)
            depth += aim * int(units)
        else:
            aim += planned_course[dir] * int(units)

    return h_pos * depth


if __name__ == "__main__":

    output1 = task1_get_planned_course(data_path)
    print(output1)

    output2 = task2_get_course_with_aim(data_path)
    print(output2)
