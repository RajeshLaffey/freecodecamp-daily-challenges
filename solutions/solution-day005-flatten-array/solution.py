def flatten(arr):
    return_value = []
    for index in arr:
        if isinstance(index, list):
            return_value += flatten(index)
        else:
            return_value.append(index)

    return return_value


# Scenario 1: One-level nested list of ints
print(flatten([1, [2, 3], 4]))  
# Expected: [1, 2, 3, 4]

# Scenario 2: Mixed nesting (list inside list) of ints
print(flatten([5, [4, [3, 2]], 1]))  
# Expected: [5, 4, 3, 2, 1]

# Scenario 3: Strings with deeper nesting
print(flatten(["A", [[["B"]]], "C"]))  
# Expected: ["A", "B", "C"]

# Scenario 4: Very deep nesting with many letters
print(flatten([["L", "M", "N"], ["O", ["P", "Q", ["R", ["S", ["T", "U"]]]]], "V", ["W", ["X", ["Y", ["Z"]]]]]))  
# Expected: ["L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# Scenario 5: Color strings with mixed nesting
print(flatten([["red", ["blue", ["green", ["yellow", ["purple"]]]]], "orange", ["pink", ["brown"]]]))  
# Expected: ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown"]
