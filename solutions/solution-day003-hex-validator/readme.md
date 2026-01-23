# Hex Color Validator (Python)

## Overview
This project implements a Python function that validates whether a given string is a valid **CSS hex color**. The solution follows standard CSS rules and demonstrates fundamental Python concepts such as string manipulation, conditionals, loops, and character validation.

## Problem Statement
Given a string, determine whether it is a valid CSS hex color.

A valid CSS hex color must:
- Start with a `#`
- Be followed by **either 3 or 6 hexadecimal characters**
- Use only characters `0–9` and `a–f` (case-insensitive)

## Solution Approach
The validator applies a clear sequence of rule-based checks:

1. Confirm the input begins with `#`
2. Extract the characters following the `#`
3. Ensure the remaining length is exactly 3 or 6 characters
4. Verify each character is a valid hexadecimal digit (case-insensitive)

