'''
Given a snowboarder's starting stance and a rotation in degrees, determine 
their landing stance.

A snowboarder's stance is either "Regular" or "Goofy".
Trick rotations are multiples of 90 degrees. Positive indicates 
clockwise rotation, and negative indicate counter-clockwise rotation.

The landing stance flips every 180 degrees of rotation.
For example, given "Regular" and 90, return "Regular". Given "Regular" 
and 180 degrees, return "Goofy".
'''

def get_landing_stance(stance, degree):
    
    if not isinstance(degree, int):
        raise ValueError("Please enter an integer")
    
    if stance not in ("Regular", "Goofy"):
        raise ValueError("Please enter 'Regular' or 'Goofy' Stance")
    
    flips = (abs(degree) // 180) % 2
    
    if flips == 1:
        if stance == "Goofy":
            stance = "Regular"
        else:
            stance = "Goofy"
    
    return stance
   

print(get_landing_stance("Regular", 90))     # Expected: Regular
print(get_landing_stance("Regular", 180))    # Expected: Goofy
print(get_landing_stance("Goofy", -270))     # Expected: Regular
print(get_landing_stance("Regular", 2340))   # Expected: Goofy
print(get_landing_stance("Goofy", 2160))     # Expected: Goofy
print(get_landing_stance("Goofy", -540))     # Expected: Regular

