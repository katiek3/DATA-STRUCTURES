import random 
import time 
# Constants 
Minimum_random_value: int = -10
Maximum_random_value: int = 10 
time_limit: int = 60*1_000_000_000 
matrix_size: int = 15

# Recursive Determinant
def determinant(A: list[list[int]]) -> int:
    """Compute the determinant of a square matrix A (list of lists)."""
    # Number of rows and columns 
    # Store the determinant
    n: int = len(A)
    det: int = 0

    # Trivial case: 1x1 matrix
    if n == 1:
        det = A[0][0]
    # Base case: 2x2 matrix 
    elif n == 2:
        # Determinant formula ad-bc
        det = A[0][0]*A[1][1] - A[0][1]*A[1][0]
    # Recursive case: matricies larger than 2x2
    else:
        # Loop over columns of the first row 
        for j in range(n):
            # Build the minor matrix exclusing the first row and current column
            minor_matrix = [[0 for _ in range(n-1)] 
                                        for _ in range(n-1)]
            # Fill in minor matrix 
            # Begin from row 1 
            for row in range(1,n):
                column_index = 0
                for col in range(n):
                    # Skip current column 
                    if col != j:
                        # Copy all elements except the first row and the current column j
                        minor_matrix[row-1][column_index] = A[row][col]
                        column_index += 1
            # Add to determinant
            det += ((-1)** j) * A[0][j] * determinant(minor_matrix)
    return det 
    
# Generate a random non-zero matrix 
def random_matrix(rows: int, cols: int, min_val:int=Minimum_random_value, 
                  max_val: int =Maximum_random_value) -> list[list[int]]:

    """Generate a random matrix with given dimensions and value range."""

    # Initialize a rows x cols matrix with zeros 
    matrix_random = [[0 for _ in range(cols)] for _ in range(rows)]

    # Nested loop to iterate over every element of the matrix 
    for i in range(rows):
        for j in range(cols):
            value: int = 0

            # Zero values in the matrix are randomized integers between default 
            # min and max values 
            # Loop continues generating new number until it is non-zero
            while value ==0:
                value = random.randint(min_val, max_val)

            # Assign non-zero value to the matrix at position [i][j]
            matrix_random[i][j] = value 

    # Return complete matrix 
    return matrix_random

# Gaussian Elimination Determinant 
def gaussian_elimination(A: list[list[int]]) -> None:
    """
    Implement the Gaussian elimination algorithm. 
    Test and measure the time it requries to solve a system of n x n.

    The algorithm transforms the matrix into an upper-triangle form
    by using a leading element (first non-zero number from the top 
    of the column that has not been used) in each column to eliminate
    the elements below it. 

    """
    # Initalize number of rows and columns 
    n: int = len(A)

    # Copy matrix to not modify the original
    # Initialize n x n zero matrix
    M = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # Copy each element from A into M
            M[i][j] = A[i][j]

    # Perform elimination in order to creat the upper-triangular matrix
    # Loop over each leading column and row 
    for i in range(n):

        # Flag if there is a non-zero leading element
        leading_element_found: bool = False
        # Store row index if there is a leading element
        leading_element_row: int = i
        # Begin at current row and used to search downward for a non zero leading element
        check_row: int = i

        # Loop through every row below the current one 
        while check_row < n:
            # If the element in the column is non-zero 
            if M[check_row][i] != 0:
                # If leading element is not found yes 
                if not leading_element_found:
                    # Set the current row as the leading row
                    leading_element_row = check_row
                    # Flag that leading was found 
                    leading_element_found = True
            # Move to the next row 
            check_row += 1

        # Swap leading element row with current row if the leading element is not in the current row
        if leading_element_row != i:
            M[i], M[leading_element_row] = M[leading_element_row], M[i]

        # Eliminate entries below leading element 
        # Continue if leading element exists
        if leading_element_found:
            # Loop over all rows below the leading element
            for k in range (i+1, n):
                # Leading element
                a: int = M[i][i]
                # Element in current row to eliminate
                b: int = M[k][i]
                # Eliminate if element not already zero
                if b != 0:
                    #Loop over columns starting at leading column
                    for c in range(i,n):
                        # Eliminate element 
                        M[k][c] = a * M[k][c] - b * M[i][c]
    return None

def largest_determinant_matrix(max_size: int) -> None:
    """
    Measure recursive determinant and Gaussian elimination times for square 
    matrices from size 1 to max_size. Stops computing the recursive determinant 
    once the time exceeds time_limit, but continues Gaussian timing.
    """
    # Begin with smallest matrix size
    size: int = 1
    # Stop recursive determinant computation if it takes too long
    stop_recursive_det: bool = False

    # Loop through all matrix sizes from 1 to max_size
    while size <= max_size:
        # Generate random non-zero matrix of current set size 
        matrix: list[list[int]] = random_matrix(size, size)

        # Measure recursive determinant if not stopped
        if not stop_recursive_det:
            # Record start time of recursive determinant calculation
            start_time = time.time_ns()
            # Calculate determinant recusively
            determinant_value = determinant(matrix)
            # Record the end time
            end_time = time.time_ns()
            # Compute the elapsed time 
            time_elapsed = end_time - start_time

            # If recurvie determinant takes longer than time_limit, stop
            if time_elapsed > time_limit:
                stop_recursive_det = True  
        else:
            # If recursvie determinant was stopped, return None
            determinant_value = None
            time_elapsed = None

        # Gaussian elimination time 
        start_time_gauss = time.time_ns()
        gaussian_elimination(matrix)
        end_time_gauss = time.time_ns()
        # Elapsed time for Gaussian elimination
        time_elapsed_gauss = end_time_gauss - start_time_gauss

        # Print results for current matrix size 
        print(f"Size: {size} x {size}, Recursive time (ns): {time_elapsed}, "
              f"Determinant: {determinant_value}, Gaussian time (ns): {time_elapsed_gauss}")
        
        # Move to next matrix size 
        size += 1
# Run for matricies up to size 15 
largest_determinant_matrix(matrix_size)

# Test Case 
A = [[1]]
print(determinant(A))

B = [[1, 2],
     [3, 4]]
print(determinant(B)) 

C = [[2, 0, 1],
     [3, 0, 0],
     [5, 1, 1]]
print(determinant(C))  
