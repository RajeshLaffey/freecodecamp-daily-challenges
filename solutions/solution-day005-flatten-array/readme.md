# Day 04 – Array Flattening (Recursive)

## Overview
This project implements a Python function that flattens an array containing nested arrays into a single, one-dimensional array. The solution preserves the original order of elements and demonstrates fundamental Python concepts such as recursion, type checking, loops, and list operations.

## Problem Statement
Given an array that may contain nested arrays, return a new array with all values flattened into a single, one-dimensional array while retaining the original order of the elements.

### Example
- Input: [1, [2, 3], 4]
- Output: [1, 2, 3, 4]

The function must correctly handle arrays nested to any depth.

## Solution Requirements
The flattening function must:

- Accept an array containing values and nested arrays
- Traverse elements in their original order
- Recursively process nested arrays
- Return a new flattened array
- Preserve the sequence of all values

## Solution Approach
The solution uses recursion to handle nested arrays of arbitrary depth:

1. Initialize an empty list to store flattened values
2. Iterate through each element in the input array
3. If an element is a list:
   - Recursively call the flatten function on that list
   - Merge the returned values into the current result list
4. If an element is not a list:
   - Append it directly to the result list
5. Return the fully flattened list

This approach ensures consistent handling of nested structures while maintaining the original order of elements.

## Key Concepts Demonstrated
- Recursion
- Type checking with `isinstance`
- List iteration
- Problem decomposition
