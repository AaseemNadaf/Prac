import math
import random

def objective_function(x):
    """Example objective function to minimize: f(x) = x^2"""
    return x * x

def simulated_annealing(max_iter=100, temp=100, cooling=0.9):
    """Simplified simulated annealing algorithm"""
    # Initialize with random starting point
    current = random.uniform(-10, 10)
    best = current
    best_cost = objective_function(best)
    
    for i in range(max_iter):
        # Stop if temperature becomes too low
        if temp < 0.01:
            break
            
        # Generate neighbor by adding random step
        neighbor = current + random.uniform(-1, 1)
        
        # Calculate current and neighbor costs
        current_cost = objective_function(current)
        neighbor_cost = objective_function(neighbor)
        
        # Decide whether to accept neighbor
        if neighbor_cost < current_cost:
            # Always accept better solutions
            current = neighbor
        else:
            # Accept worse solutions with some probability
            p = math.exp((current_cost - neighbor_cost) / temp)
            if random.random() < p:
                current = neighbor
        
        # Update best solution if needed
        if objective_function(current) < best_cost:
            best = current
            best_cost = objective_function(best)
            print("Iteration %d: x = %g, cost = %g" % (i, best, best_cost))
        
        # Cool down temperature
        temp *= cooling
    
    return best, best_cost

# Example usage
if __name__ == "__main__":
    print("Starting simulated annealing")
    solution, cost = simulated_annealing(max_iter=200)
    print("\nFinal solution: x = %g, cost = %g" % (solution, cost))