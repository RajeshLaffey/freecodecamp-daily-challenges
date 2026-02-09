## Overview
This project implements a Python function to calculate the total penalty distance a biathlon athlete must ski based on their shooting performance across multiple rounds. The solution focuses on correctness, input validation, and readable logic.

## Problem Statement
Given an array of integers where each value represents the number of targets hit in a single biathlon round, calculate the total penalty distance incurred.

- Each round consists of **5 targets**
- Each missed target results in a **150-meter penalty loop**
- The final output should be the **total penalty distance in meters**

## Solution Requirements
The solution must:
- Accept a list of integers as input
- Validate that each value is an integer
- Ensure all values are within the valid range of **0 to 5**
- Accurately calculate penalty distance based on missed targets
- Raise clear errors for invalid input

## Solution Approach
The function iterates through each round’s target count, validates the input, and calculates the penalty distance by converting missed targets into meters. A running total is maintained and returned at the end.

This approach ensures:
- Immediate failure on invalid input (defensive programming)
- Clear, readable logic
- Linear time complexity proportional to the number of rounds

## Key Concepts Demonstrated
- Functions
- Lists
- Loops
- Conditional logic
- Input validation
- Error handling
- Basic arithmetic
