def generate_latin_square(n):
    """
    Generate an n x n Latin square with numbers 1 to n
    appearing exactly once in each row and column.
    
    Args:
        n: The size of the Latin square
        
    Returns:
        A 2D list representing the Latin square
    """
    # Initialize an empty matrix
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    
    # Fill the first row with 1 to n
    for j in range(n):
        matrix[0][j] = j + 1
    
    # Fill the rest of the matrix using a simple pattern
    # Each subsequent row is the previous row shifted right by 1
    for i in range(1, n):
        for j in range(n):
            matrix[i][j] = matrix[i-1][(j+1) % n]
    
    return matrix

def print_matrix(matrix):
    """
    Print the matrix in a readable format
    
    Args:
        matrix: 2D list to print
    """
    for row in matrix:
        # Using join instead of f-strings to format output
        print(" ".join(str(num) for num in row))

# Example usage
if __name__ == "__main__":
    n = int(input("Enter the size of the Latin square (n): "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        latin_square = generate_latin_square(n)
        print("\nLatin Square " + str(n) + " x " + str(n) + ":")
        print_matrix(latin_square)