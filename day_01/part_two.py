"""--- Part Two ---
The Elves in accounting are thankful for your help; one of them even offers you
a starfish coin they had left over from a past vacation. They offer you a second
 one if you can find three numbers in your expense report that meet the same
 criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366,
and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to
2020?"""

from day_01 import lib


def main():
    low, mid, high = lib.find_three_numbers_summing_to(
        input_numbers=lib.read_input_file(),
        target=2020)
    print(f"Correct answer is: {low*mid*high}")  # 49214880


if __name__ == '__main__':
    main()
