# https://adventofcode.com/2021/day/10

from pathlib import Path
from typing import List

base_path = Path(__file__).parents[0].resolve()
data_path = base_path / "input" / "input10.txt"


char_pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}


def get_illegal_scores(line: str):
    "Get the illegar score from one line."

    char_points = {")": 3, "]": 57, "}": 1197, ">": 25137}
    len_line = len(line.replace("\n", ""))
    left_part = []
    # Loop through characters
    for i in range(len_line):
        if line[i] in char_pairs:
            left_part.append(line[i])
        else:
            if line[i] == char_pairs[left_part[-1]]:
                left_part.pop()
            else:
                # Return corrupted string
                return left_part, char_points[line[i]]
    # Return incomplete string
    return left_part, 0


def get_multiplied_score(input: List[chr]) -> int:
    "Get multiplied score of incomplete string."

    char_points = {")": 1, "]": 2, "}": 3, ">": 4}
    score = 0
    for i in range(len(input) - 1, -1, -1):
        score = score * 5 + char_points[char_pairs[input[i]]]
    return score


def task1_find_corrupted_character(input_file_path: str) -> int:
    "Find the points of illegal characters."

    file = open(input_file_path, "r")
    Lines = file.readlines()
    score = 0
    for line in Lines:
        left_part, score0 = get_illegal_scores(line)
        score += score0
    return score


def task2_find_corrupted_character(input_file_path: str) -> int:
    "Find the points of illegal characters."

    file = open(input_file_path, "r")
    Lines = file.readlines()
    score = []
    for line in Lines:
        left_part, score0 = get_illegal_scores(line)
        if score0 == 0:
            score.append(get_multiplied_score(left_part))
    score.sort()
    # return the middle score
    return score[int((len(score) - 1) / 2)]


if __name__ == "__main__":

    output1 = task1_find_corrupted_character(data_path)
    print(output1)

    output2 = task2_find_corrupted_character(data_path)
    print(output2)
