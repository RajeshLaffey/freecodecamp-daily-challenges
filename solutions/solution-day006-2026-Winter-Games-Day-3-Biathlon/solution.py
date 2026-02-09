'''
Given an array of integers, where each value represents the number of targets 
hit in a single round of a biathlon, return the total penalty distance the 
athlete must ski.

Each round consists of 5 targets.
Each missed target results in a 150 meter penalty loop.
'''

def calculate_penalty_distance(target_hits):
    distance = 0
         
    for num in target_hits:
        if not isinstance(num, int):
            raise ValueError("Please enter integers only.")
            
        if num < 0 or num > 5:
            raise ValueError("Please enter values between 0 and 5.")
        
        distance += (5-num) * 150
        
    
    return distance

# Scenario 1
# Input: [4, 4]
# Expected result: 300
print(calculate_penalty_distance([4,4]))

# Scenario 2
# Input: [5, 5]
# Expected result: 0
print(calculate_penalty_distance([5, 5]))

# Scenario 3
# Input: [4, 5, 3, 5]
# Expected result: 450
print(calculate_penalty_distance([4, 5, 3, 5]))

# Scenario 4
# Input: [5, 4, 5, 5]
# Expected result: 150
print(calculate_penalty_distance([5, 4, 5, 5]))

# Scenario 5
# Input: [4, 3, 0, 3]
# Expected result: 1500
print(calculate_penalty_distance([4, 3, 0, 3]))



