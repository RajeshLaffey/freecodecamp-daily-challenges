# Day 03 - Number Pattern Generator

## Overview
This project implements a Python function that generates a simple number pattern as a string. The solution demonstrates fundamental Python concepts such as input validation, conditionals, loops, string construction, and formatting.

## Problem Statement
Given a positive integer `n`, return a string containing all integers from **1 to n (inclusive)** separated by a single space.

The function must also handle invalid inputs:

- If the argument is **not an integer**, return: `Argument must be an integer value.`
- If the argument is **less than 1**, return: `Argument must be an integer greater than 0.`

## Solution Approach
The function follows a straightforward, rule-based sequence of checks:

1. **Validate type**
   - Confirm the argument is an integer using `isinstance(n, int)`

2. **Validate range**
   - Confirm the integer is at least 1 (`n < 1` is invalid)

3. **Generate the pattern using a loop**
   - Use a `for` loop from `1` to `n` (inclusive)
   - Append each number to a string with spaces between values

4. **Format the final output**
   - Ensure the returned string has no trailing space

## Example
```python
number_pattern(4)
