
# Sum of Squares Challenge

## Description

This program calculates the sum of squares of given integers, excluding any negative values. It processes multiple test cases as specified by the input format.

## Requirements

- Python 3.11 or higher
- Standard library packages only

## Input Format

1. The first line contains an integer **N** (1 ≤ N ≤ 100), indicating the number of test cases.
2. Each test case consists of:
   - A line with an integer **X** (0 < X ≤ 100), indicating the number of integers to follow.
   - A line with **X** space-separated integers **Yₙ** (-100 ≤ Yₙ ≤ 100).

## Output Format

- For each test case, print the calculated sum of squares of the integers, excluding any negatives.
- There should be no output until all the input has been received, and no blank lines between test case solutions.

## Sample Input

2
4
3 -1 1 14
5
9 6 -53 32 16
## Sample Output
206
1397

## Code Structure

The solution is implemented in a single Python file, `main.py`, which contains the following functions:

- `main()`: The entry point of the program that reads input and initiates processing.
- `caseRecurse(caseNo, sumList)`: A recursive function that handles each test case.
- `squareSum(integerNo, numbers, currentSum)`: A recursive function that calculates the sum of squares of non-negative integers.
- `printSums(caseNo, sumList, counter)`: A recursive function that prints the results.

## How to Run

1. Make sure you have Python 3.11 or higher installed on your system.
2. Save the code in a file named `main.py`.
3. Run the program from the command line or terminal:
   ```bash
   python3 main.py
