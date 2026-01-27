def number_pattern(n):
    pattern = ''

    if not isinstance(n, int): 
        return 'Argument must be an integer value.'
    
    if n < 1:
        return 'Argument must be an integer greater than 0.'

    for i in range(1, n+1):
        convi = str(i)
        pattern += convi + " "
    
    pattern = pattern.strip()
    return pattern


# --------------------------
# Test Scenarios
# --------------------------

# Valid input
print(number_pattern(4))    # Expected: "1 2 3 4"
print(number_pattern(1))    # Expected: "1"
print(number_pattern(10))   # Expected: "1 2 3 4 5 6 7 8 9 10"

# Invalid input: less than 1
print(number_pattern(0))    # Expected: "Argument must be an integer greater than 0."
print(number_pattern(-2))   # Expected: "Argument must be an integer greater than 0."

# Invalid input: not an integer
print(number_pattern("4"))  # Expected: "Argument must be an integer value."
print(number_pattern(3.5))  # Expected: "Argument must be an integer value."
print(number_pattern(None)) # Expected: "Argument must be an integer value."
