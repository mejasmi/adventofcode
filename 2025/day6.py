"""--- Day 6: Trash Compactor ---
After helping the Elves in the kitchen, you were taking a break and helping them re-enact a movie scene when you over-enthusiastically jumped into the garbage chute!

A brief fall later, you find yourself in a garbage smasher. Unfortunately, the door's been magnetically sealed.

As you try to find a way out, you are approached by a family of cephalopods! They're pretty sure they can get the door open, but it will take some time. While you wait, they're curious if you can help the youngest cephalopod with her math homework.

Cephalopod math doesn't look that different from normal math. The math worksheet (your puzzle input) consists of a list of problems; each problem has a group of numbers that need to be either added (+) or multiplied (*) together.

However, the problems are arranged a little strangely; they seem to be presented next to each other in a very long horizontal list. For example:

123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
Each problem's numbers are arranged vertically; at the bottom of the problem is the symbol for the operation that needs to be performed. Problems are separated by a full column of only spaces. The left/right alignment of numbers within each problem can be ignored.

So, this worksheet contains four problems:

123 * 45 * 6 = 33210
328 + 64 + 98 = 490
51 * 387 * 215 = 4243455
64 + 23 + 314 = 401
To check their work, cephalopod students are given the grand total of adding together all of the answers to the individual problems. In this worksheet, the grand total is 33210 + 490 + 4243455 + 401 = 4277556.

Of course, the actual worksheet is much wider. You'll need to make sure to unroll it completely so that you can read the problems clearly.

Solve the problems on the math worksheet. What is the grand total found by adding together all of the answers to the individual problems?

Your puzzle answer was 6299564383938.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
The big cephalopods come back to check on how things are going. When they see that your grand total doesn't match the one expected by the worksheet, they realize they forgot to explain how to read cephalopod math.

Cephalopod math is written right-to-left in columns. Each number is given in its own column, with the most significant digit at the top and the least significant digit at the bottom. (Problems are still separated with a column consisting only of spaces, and the symbol at the bottom of the problem is still the operator to use.)

Here's the example worksheet again:

123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
Reading the problems right-to-left one column at a time, the problems are now quite different:

The rightmost problem is 4 + 431 + 623 = 1058
The second problem from the right is 175 * 581 * 32 = 3253600
The third problem from the right is 8 + 248 + 369 = 625
Finally, the leftmost problem is 356 * 24 * 1 = 8544
Now, the grand total is 1058 + 3253600 + 625 + 8544 = 3263827.

Solve the problems on the math worksheet again. What is the grand total found by adding together all of the answers to the individual problems?"""

import numpy as np

# file_path = "data/test_d6.txt"

file_path = "data/input_day6.txt"

FIRST_PART = False

if __name__ == "__main__":

    checksum = 0

    with open(file=file_path, mode="r+") as file:
        lines = file.readlines()
        operations = lines[-1].strip().split()
        sums = np.zeros(shape=(1, len(operations)), dtype=int)
        products = np.ones(shape=(1, len(operations)), dtype=int)


        if FIRST_PART:
            for line in lines[:-1]:
                row_num = [int(x) for x in line.strip().split()]
                for j, number in enumerate(row_num):
                    sums[0][j] = sums[0][j] + number
                    products[0][j] = products[0][j] * number
            for i, symbol in enumerate(operations):
                if symbol == "+":
                    checksum += sums[0][i]
                elif symbol == "*":
                    checksum += products[0][i]
        else:
            char_matrix = [[" "] for _ in range(len(lines[0].rstrip("\n")))]
            for line in lines[:-1]:
                for c, ch in enumerate(line.rstrip("\n")):
                    char_matrix[c].append(ch)
            statement_numbers =[]
            column_statement = []
            for k in range(len(char_matrix)):
                if char_matrix[k] == [" "]* len(char_matrix[0]):
                    # if there is a column with only spaces, then it is a separator
                    if len(column_statement) > 0:
                        numbers = []
                        for n in range(len(column_statement)):
                            numbers.append(int("".join(column_statement[:][n]).strip()))
                        statement_numbers.append(numbers)
                        column_statement = []
                else:
                    column_statement.append(char_matrix[k])

            # repeat the number extraction for the last column statement
            if len(column_statement) > 0:
                numbers = []
                for n in range(len(column_statement)):
                    numbers.append(int("".join(column_statement[:][n]).strip()))
                statement_numbers.append(numbers)
                column_statement = []

            for j, statement in enumerate(statement_numbers):
                for number in statement:
                    sums[0][j] = sums[0][j] + number
                    products[0][j] = products[0][j] * number
            for i, symbol in enumerate(operations):
                if symbol == "+":
                    checksum += sums[0][i]
                elif symbol == "*":
                    checksum += products[0][i]

    print("Final checksum", checksum, ".")