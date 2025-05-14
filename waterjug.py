def water_jug_problem():
    # Initial state: both jugs are empty
    jug4 = 0  # 4-liter jug
    jug3 = 0  # 3-liter jug
    
    print("Step 0: 4-liter jug = " + str(jug4) + ", 3-liter jug = " + str(jug3))
    
    # Step 1: Fill the 4-liter jug
    jug4 = 4
    print("Step 1: 4-liter jug = " + str(jug4) + ", 3-liter jug = " + str(jug3))
    
    # Step 2: Pour water from 4-liter jug to 3-liter jug
    water_to_transfer = min(jug4, 3 - jug3)
    jug4 -= water_to_transfer
    jug3 += water_to_transfer
    print("Step 2: 4-liter jug = " + str(jug4) + ", 3-liter jug = " + str(jug3))
    
    # Step 3: Empty the 3-liter jug
    jug3 = 0
    print("Step 3: 4-liter jug = " + str(jug4) + ", 3-liter jug = " + str(jug3))
    
    # Step 4: Pour the remaining 1 liter from 4-liter jug to 3-liter jug
    water_to_transfer = min(jug4, 3 - jug3)
    jug4 -= water_to_transfer
    jug3 += water_to_transfer
    print("Step 4: 4-liter jug = " + str(jug4) + ", 3-liter jug = " + str(jug3))
    
    # Step 5: Fill the 4-liter jug again
    jug4 = 4
    print("Step 5: 4-liter jug = " + str(jug4) + ", 3-liter jug = " + str(jug3))
    
    # Step 6: Pour water from 4-liter jug to fill 3-liter jug
    water_to_transfer = min(jug4, 3 - jug3)
    jug4 -= water_to_transfer
    jug3 += water_to_transfer
    print("Step 6: 4-liter jug = " + str(jug4) + ", 3-liter jug = " + str(jug3))
    
    # At this point, we have 2 liters in the 4-liter jug
    print("\nResult: 2 liters measured in the 4-liter jug!")

if __name__ == "__main__":
    print("Water Jug Problem: Measure exactly 2 liters using jugs of capacity 4 and 3 liters\n")
    water_jug_problem()