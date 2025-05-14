import math

# Calculate total route distance
def route_distance(route, cities):
    dist = 0
    for i in range(len(route)):
        j = (i + 1) % len(route)  # Next city (wraps around to start)
        city1, city2 = cities[route[i]], cities[route[j]]
        dist += math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)
    return dist

# Hill Climbing algorithm for TSP
def hill_climbing(cities, max_attempts=100):
    # Start with cities in order 0,1,2,...
    current_route = list(range(len(cities)))
    best_distance = route_distance(current_route, cities)
    
    attempts = 0
    improved = True
    
    while improved and attempts < max_attempts:
        improved = False
        attempts += 1
        
        # Try swapping each possible pair of cities
        for i in range(len(cities)):
            for j in range(i+1, len(cities)):
                # Create new route with cities i and j swapped
                new_route = current_route.copy()
                new_route[i], new_route[j] = new_route[j], new_route[i]
                
                # Calculate new distance
                new_distance = route_distance(new_route, cities)
                
                # If better, accept this route
                if new_distance < best_distance:
                    current_route = new_route
                    best_distance = new_distance
                    improved = True
                    break  # Found improvement, start over with new route
            
            if improved:
                break
    
    return current_route, best_distance

# Main program
if __name__ == "__main__":
    # Predefined cities (x,y coordinates)
    cities = [
        (0, 0),    # City 0
        (10, 20),  # City 1
        (20, 30),  # City 2
        (30, 10),  # City 3
        (40, 30),  # City 4
        (30, 40),  # City 5
        (20, 50),  # City 6
        (10, 40)   # City 7
    ]
    
    # Solve TSP with hill climbing
    best_route, best_dist = hill_climbing(cities)
    
    # Print the shortest route found and its distance
    print(best_route)
    print(best_dist)

"""
Let n = number of cities

 Time Complexity:
Outer loop (max max_attempts): O(max_attempts)

Inner nested loop (all city pairs): O(n^2)

For each pair swap, route_distance() takes O(n)

Overall Time Complexity: O(max_attempts × n^3)

 Space Complexity:
current_route, new_route, city coordinates: O(n)

Overall Space Complexity: O(n)
"""