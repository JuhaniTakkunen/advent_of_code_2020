from functools import lru_cache
from pathlib import Path

"""--- Day 3: Toboggan Trajectory --- With the toboggan login problems 
resolved, you set off toward the airport. While travel by toboggan might be 
easy, it's certainly not safe: there's very minimal steering and the area is 
covered in trees. You'll need to see which angles will take you near the 
fewest trees. 

Due to the local geology, trees in this area only grow on exact integer 
coordinates in a grid. You make a map (your puzzle input) of the open squares 
(.) and trees (#) you can see. For example: 

..##....... #...#...#.. .#....#..#. ..#.#...#.# .#...##..#. ..#.##..... 
.#.#.#....# .#........# #.##...#... #...##....# .#..#...#.# These aren't the 
only trees, though; due to something you read about once involving arboreal 
genetics and biome stability, the same pattern repeats to the right many times: 

..##.........##.........##.........##.........##.........##.......  ---> 
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#.. 
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#. 
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.# 
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#. 
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  ---> 
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....# 
.#........#.#........#.#........#.#........#.#........#.#........# 
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#... 
#...##....##...##....##...##....##...##....##...##....##...##....# 
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  ---> You 
start on the open square (.) in the top-left corner and need to reach the 
bottom (below the bottom-most row on your map). 

The toboggan can only follow a few specific slopes (you opted for a cheaper 
model that prefers rational numbers); start by counting all the trees you 
would encounter for the slope right 3, down 1: 

From your starting position at the top-left, check the position that is right 
3 and down 1. Then, check the position that is right 3 and down 1 from there, 
and so on until you go past the bottom of the map. 

The locations you'd check in the above example are marked here with O where 
there was an open square and X where there was a tree: 

..##.........##.........##.........##.........##.........##.......  ---> 
#..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#.. 
.#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#. 
..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.# 
.#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#. 
..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  ---> 
.#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....# 
.#........#.#........X.#........#.#........#.#........#.#........# 
#.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#... 
#...##....##...##....##...#X....##...##....##...##....##...##....# 
.#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  ---> In 
this example, traversing the map using this slope would cause you to 
encounter 7 trees. 

Starting at the top-left corner of your map and following a slope of right 3 
and down 1, how many trees would you encounter? 

Your puzzle answer was 265.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two --- Time to check the rest of the slopes - you need to minimize 
the probability of a sudden arboreal stop, after all. 

Determine the number of trees you would encounter if, for each of the 
following slopes, you start at the top-left corner and traverse the map all 
the way to the bottom: 

Right 1, down 1. Right 3, down 1. (This is the slope you already checked.) 
Right 5, down 1. Right 7, down 1. Right 1, down 2. In the above example, 
these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied 
together, these produce the answer 336. 

What do you get if you multiply together the number of trees encountered on 
each of the listed slopes? 

Answer: 
 

Although it hasn't changed, you can still get your puzzle input.

You can also [Share] this puzzle."""


@lru_cache
def read_data():
    fp = Path("input_data.txt")
    data = fp.read_text().splitlines()
    return data


def check_if_tree(x, y):
    data = read_data()

    if y >= len(data):
        return None

    row_length = len(data[0])
    while x >= row_length:
        x -= row_length
    return data[y][x] == "#"


def calc_slope(x_inc, y_inc):
    x = 0
    y = 0
    trees = 0

    while True:
        res = check_if_tree(x, y)
        if res is True:
            trees += 1
        elif res is None:
            break

        x += x_inc
        y += y_inc
    print(x_inc, y_inc, trees)
    return trees


def main():
    res = 1
    res *= calc_slope(x_inc=1, y_inc=1)
    res *= calc_slope(x_inc=3, y_inc=1)
    res *= calc_slope(x_inc=5, y_inc=1)
    res *= calc_slope(x_inc=7, y_inc=1)
    res *= calc_slope(x_inc=1, y_inc=2)
    print("total: ", res)


if __name__ == '__main__':
    main()
