## Overview
This project implements a Python function that determines a snowboarder’s **landing stance** after performing a rotational trick. Given a starting stance and a rotation angle in degrees, the function calculates whether the rider lands in the same stance or switches stances based on standard snowboard rotation rules.

The solution emphasizes clean logic, input validation, and correct handling of large and negative rotations.

---

## Problem Statement
A snowboarder begins a trick in one of two stances:
- **Regular**
- **Goofy**

Trick rotations:
- Are always multiples of **90 degrees**
- Can be **positive** (clockwise) or **negative** (counter-clockwise)

Rules:
- The snowboarder’s stance **flips every 180 degrees** of rotation
- Direction of rotation does **not** affect stance
- The function must return the correct landing stance

### Examples
- Regular + 90° → Regular  
- Regular + 180° → Goofy  
- Goofy + −270° → Regular  

---

## Solution Requirements
The solution must:
- Accept a starting stance (`"Regular"` or `"Goofy"`)
- Accept a rotation in degrees (integer)
- Handle large rotations and negative values
- Validate inputs and raise meaningful errors
- Correctly determine whether the stance flips based on rotation

---

## Solution Approach
The approach is based on counting how many **180-degree rotations** occur during the trick:

1. Normalize the rotation using the absolute value (direction does not matter).
2. Divide by `180` to calculate how many stance flips occur.
3. Use modulo (`% 2`) to determine whether the number of flips is odd or even:
   - **Even** → stance remains the same
   - **Odd** → stance switches
4. Return the resulting stance.

This approach keeps the logic concise, readable, and scalable for very large degree values.

---

## Key Concepts Demonstrated
This project demonstrates the following Python concepts:

- Function definition and return values
- Input validation and exception handling (`ValueError`)
- Integer arithmetic and floor division (`//`)
- Modulo operations (`%`) for parity checks
- Conditional logic (`if / else`)
- Use of built-in functions like `abs()`
- Writing clean, readable, and maintainable code
