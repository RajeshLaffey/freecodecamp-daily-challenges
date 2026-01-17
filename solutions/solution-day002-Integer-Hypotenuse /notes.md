# Day 02 – Integer Hypotenuse

## Problem
Given two positive integers representing the lengths of the two legs of a right triangle, determine whether the hypotenuse length is an integer.

The hypotenuse is calculated using the Pythagorean theorem:  
`a² + b² = c²`

## Solution Overview
The function calculates the square of the hypotenuse (`c²`) by summing the squares of the two legs. It then uses `math.isqrt()` to compute the integer square root of that value.

To determine whether the hypotenuse is an integer:
- The integer square root is squared
- If the result equals the original `c²`, the hypotenuse is an integer

## Why this works
`math.isqrt()` returns the integer portion of a square root without using floating-point arithmetic. By squaring the result and comparing it to the original value, the function avoids precision issues that can occur when using decimals.

## Testing
The function was tested using two cases:
- `(3, 4)` → `a² + b² = 25`, which results in an integer hypotenuse
- `(3, 5)` → `a² + b² = 34`, which does not result in an integer hypotenuse

Printing the results provides a simple visual confirmation that the logic behaves as expected.

## Key Takeaway
This challenge reinforces applying mathematical formulas in Python and highlights the usefulness of integer-based operations when validating perfect squares.
