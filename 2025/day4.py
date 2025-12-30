"""--- Day 4: Printing Department ---
You ride the escalator down to the printing department. They're clearly getting ready for Christmas; they have lots of large rolls of paper everywhere, and there's even a massive printer in the corner (to handle the really big print jobs).

Decorating here will be easy: they can make their own decorations. What you really need is a way to get further into the North Pole base while the elevators are offline.

"Actually, maybe we can help with that," one of the Elves replies when you ask for help. "We're pretty sure there's a cafeteria on the other side of the back wall. If we could break through the wall, you'd be able to keep moving. It's too bad all of our forklifts are so busy moving those big rolls of paper around."

If you can optimize the work the forklifts are doing, maybe they would have time to spare to break through the wall.

The rolls of paper (@) are arranged on a large grid; the Elves even have a helpful diagram (your puzzle input) indicating where everything is located.

For example:

..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
The forklifts can only access a roll of paper if there are fewer than four rolls of paper in the eight adjacent positions. If you can figure out which rolls of paper the forklifts can access, they'll spend less time looking and more time breaking down the wall to the cafeteria.

In this example, there are 13 rolls of paper that can be accessed by a forklift (marked with x):

..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.
Consider your complete diagram of the paper roll locations. How many rolls of paper can be accessed by a forklift?

Your puzzle answer was 1409.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
Now, the Elves just need help accessing as much of the paper as they can.

Once a roll of paper can be accessed by a forklift, it can be removed. Once a roll of paper is removed, the forklifts might be able to access more rolls of paper, which they might also be able to remove. How many total rolls of paper could the Elves remove if they keep repeating this process?

Starting with the same example as above, here is one way you could remove as many rolls of paper as possible, using highlighted @ to indicate that a roll of paper is about to be removed, and using x to indicate that a roll of paper was just removed:

Initial state:
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.

Remove 13 rolls of paper:
..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.

Remove 12 rolls of paper:
.......x..
.@@.x.x.@x
x@@@@...@@
x.@@@@..x.
.@.@@@@.x.
.x@@@@@@.x
.x.@.@.@@@
..@@@.@@@@
.x@@@@@@@.
....@@@...

Remove 7 rolls of paper:
..........
.x@.....x.
.@@@@...xx
..@@@@....
.x.@@@@...
..@@@@@@..
...@.@.@@x
..@@@.@@@@
..x@@@@@@.
....@@@...

Remove 5 rolls of paper:
..........
..x.......
.x@@@.....
..@@@@....
...@@@@...
..x@@@@@..
...@.@.@@.
..x@@.@@@x
...@@@@@@.
....@@@...

Remove 2 rolls of paper:
..........
..........
..x@@.....
..@@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@x.
....@@@...

Remove 1 roll of paper:
..........
..........
...@@.....
..x@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...

Remove 1 roll of paper:
..........
..........
...x@.....
...@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...

Remove 1 roll of paper:
..........
..........
....x.....
...@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...

Remove 1 roll of paper:
..........
..........
..........
...x@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...
Stop once no more rolls of paper are accessible by a forklift. In this example, a total of 43 rolls of paper can be removed.

Start with your original diagram. How many rolls of paper in total can be removed by the Elves and their forklifts?"""

import re
import numpy as np

# file_path = "data/test_d4.txt"

file_path = "data/input_day4.txt"

FIRST_PART = False
NUM_NEIGHBOR = 4 

if __name__ == "__main__":
    access_rolls = 0

    with open(file=file_path, mode="r+") as file:
        lines = file.readlines()
        # read the whole file and place in 2D array
        shelf  = np.zeros(shape=(len(lines), len(lines[0].strip())), dtype=object)
        for i, line in enumerate(lines):
            for j, ch in enumerate(line.strip()):
                if ch == "@":
                    shelf[i][j] = 1
        
        if FIRST_PART:
            # check each position in the shelf and sum the 3x3 neighbors
            # of all ones and see if the sum is less than or equal to NUM_NEIGHBOR
            for i in range(shelf.shape[0]):
                for j in range(shelf.shape[1]):
                    if shelf[i][j] == 1:
                        # get the neighbors
                        row_start = max(0, i-1)
                        row_end = min(shelf.shape[0], i+2)
                        col_start = max(0, j-1)
                        col_end = min(shelf.shape[1], j+2)
                        sub_array = shelf[row_start:row_end, col_start:col_end]
                        neighbor_sum = np.sum(sub_array)
                        if neighbor_sum < NUM_NEIGHBOR+1: #fewer than NUM_NEIGHBOR + 1 becouse it sums itself
                            access_rolls += 1
        else:
            # keep removing accessible rolls until no more can be removed
            # for first pass select all positions with rolls
            adjacent_to_remove = [(m,n) for m in range(shelf.shape[0]) for n in range(shelf.shape[1]) if shelf[m][n]==1]
            while len(adjacent_to_remove) > 0:
                new_adjacent_to_remove = []
                for (i,j) in adjacent_to_remove:
                    # if position is already removed, continue
                    if shelf[i][j] != 1:
                        continue
                    # get the neighbors
                    row_start = max(0, i-1)
                    row_end = min(shelf.shape[0], i+2)
                    col_start = max(0, j-1)
                    col_end = min(shelf.shape[1], j+2)
                    neighbor_sum = np.sum(shelf[row_start:row_end, col_start:col_end])
                    if neighbor_sum < NUM_NEIGHBOR+1: #fewer than NUM_NEIGHBOR + 1 becouse it sums itself
                        # remove the roll
                        shelf[i][j] = 0
                        access_rolls += 1
                        # add neighbors to the list to check in next iteration
                        for ni in range(row_start, row_end):
                            for nj in range(col_start, col_end):
                                if shelf[ni][nj] == 1:
                                    new_adjacent_to_remove.append((ni, nj))
                # remove duplicates
                adjacent_to_remove = list(set(new_adjacent_to_remove))

print("Rolls that can be accessed: ", access_rolls, ".")