from pathlib import Path
from typing import Iterable

INPUT_FILE = "input_data.txt"


def read_input_file() -> Iterable[int]:
    fp = Path(INPUT_FILE)
    return (int(x) for x in fp.read_text().split())


def find_two_numbers_summing_to(input_numbers: Iterable[int], target: int):
    """ The code is working, ie. it gives correct result.
    There might be some bugs / edge cases, so not for real use"""
    sorted_res = sorted(input_numbers)

    low_number = sorted_res.pop(0)
    high_number = sorted_res.pop()

    while True:
        # Option 1: Advance from lower numbers
        if low_number + high_number < target:
            low_number = sorted_res.pop(0)

        # Option 2: Advance from higher numbers
        while low_number + high_number > target:
            high_number = sorted_res.pop()

        # Are we there yet?
        if low_number + high_number == target:
            return low_number, high_number


def find_three_numbers_summing_to(input_numbers: Iterable[int], target: int):
    """ The code is working, ie. it gives correct result.
    There might be some bugs / edge cases, so not for real use"""

    sorted_res = sorted(input_numbers)
    low_number = sorted_res.pop(0)
    high_number = sorted_res.pop()
    while True:
        # Try moving mid number
        fo = [low_number] + sorted_res + [high_number]
        for mid_number in fo:
            for high_number_2 in fo:
                total = low_number + mid_number + high_number_2
                if total == target:
                    return low_number, mid_number, high_number_2
                elif total > target:
                    print("break no bueno", low_number, mid_number, high_number_2, total)
                    break
                print("conti no bueno", low_number, mid_number, high_number_2, total)

        # Option 1: Advance from lower numbers
        if low_number * 2 + high_number < target:
            low_number = sorted_res.pop(0)

        # Option 2: Advance from higher numbers
        while low_number * 2 + high_number > target:
            high_number = sorted_res.pop()
