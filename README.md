# Code Pairing Assignment

## Overview

This assignment consists of a set of Python programming problems of varying difficulty, grouped as Basic, Intermediate, and Advanced. Each problem is implemented as a method in the `ProblemSolver` class (see `main.py`). Comprehensive tests are provided in `tests.py`.

Your task is to implement or review the solutions in `main.py` so that all tests in `tests.py` pass.

## How to Run

1. Make sure you have Python 3 installed.
2. Place both `main.py` and `tests.py` in the same directory.
3. Run the tests using:
   ```
   python tests.py
   ```
   All tests should pass if your solutions are correct.

## Problem Hints & Formulas

### Basic Problems

- **Sum of Even Numbers:**  
  Only sum even numbers greater than zero.

- **Count Vowels:**  
  Count occurrences of 'a', 'e', 'i', 'o', 'u' (case-insensitive).

- **Reverse String:**  
  Use Python slicing: `text[::-1]`.

- **Is Positive:**  
  Return `True` if the number is greater than zero.

- **Find Max:**  
  Use Python's built-in `max()` function.

- **Count Occurrences:**  
  Use `str.count()`.

### Intermediate Problems

- **Longest Word:**  
  Ignore punctuation. If multiple words are longest, return the last one.

- **Is Palindrome:**  
  Ignore case and non-alphanumeric characters.  
  Formula:  
  ```
  cleaned = ''.join(char.lower() for char in text if char.isalnum())
  cleaned == cleaned[::-1]
  ```

- **Remove Duplicates:**  
  Preserve order. Use a set to track seen elements.

- **Factorial:**  
  Formula:  
  ```
  n! = n × (n-1) × ... × 1, with 0! = 1
  ```
  Raise an error for negative numbers.

- **Capitalize Words:**  
  Use `str.capitalize()` on each word.

- **Sum of Squares:**  
  Formula:  
  ```
  sum = x1^2 + x2^2 + ... + xn^2
  ```

### Advanced Problems

- **Find Pairs with Sum:**  
  Find all unique pairs of indices `(i, j)` such that `numbers[i] + numbers[j] == target`, using each index at most once.

- **Max Subarray Sum:**  
  Use Kadane's Algorithm:  
  ```
  max_sum = current_sum = numbers[0]
  for num in numbers[1:]:
      current_sum = max(num, current_sum + num)
      max_sum = max(max_sum, current_sum)
  ```
  Return 0 for an empty list.

- **Rotate List:**  
  Rotate the list to the right by `k` steps.  
  Use slicing:  
  ```
  k = k % len(numbers)
  rotated = numbers[-k:] + numbers[:-k]
  ```

- **Is Valid Parentheses:**  
  Use a stack to check for matching opening and closing brackets.

- **Merge Sorted Lists:**  
  Use two pointers to merge both lists in sorted order.

- **Fibonacci Up To n:**  
  Generate Fibonacci numbers up to and including `n`.  
  Formula:  
  ```
  F(0) = 0, F(1) = 1
  F(n) = F(n-1) + F(n-2)
  ```

## Notes

- Read the docstrings in `main.py` for additional hints.
- If you get stuck, try running the tests to see which cases fail and why.
