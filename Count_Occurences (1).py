def occurences (values: list[int], target: int) -> int: 
    """
    Count how many times the target vlaue appears in a sorted list. 

    
    This function uses binary search to find the first and last postions 
    of the target in the sorted list of integers. It does not scan the whole
    list linearly and performs indexed access only. 

    Args: 
        values (list[int]): A sorted list of integers.
        target (int): The integer value to count in the list. 

    Returns: 
        int: The number of time the target value appears in the list. 
            Returns 0 if the target is not found. 
    """
    # Perform a binary search to find first occurence of target value (smallest index where target appears)
    # Establish variables
    starting_index = 0 
    ending_index = len(values) -1
    first_occurence = -1

    # The search range is defined by starting_index and ending_index, which adjust
    # each iteration depending how the middle value compares to the target. 
    while starting_index <= ending_index:
        # Compute the middle index of the current serch range
        middle_index = (starting_index + ending_index)//2

        # If the middle value matches the target, record it as a potential first occurence
        # Then continue searching to the left to find an earlier occurence of the target value
        if values[middle_index] == target:
            first_occurence = middle_index
            ending_index = middle_index -1  

        # If the middle value is less than the target, search the right half of the list
        elif values[middle_index] < target:
            starting_index = middle_index +1

        # If the middle value is greater than the target, search the left half of the list
        else:
            ending_index = middle_index -1
        
    # Find the last occurence index of target value (largest index where target appears)
    # Reset starting and ending indicies 
    starting_index = 0 
    ending_index = len(values)-1 
    last_occurence = -1

    # Perform a binary search to locate the last occurence of the target
    while starting_index <= ending_index:
        # Compute the middle index of the current search range
        middle_index = (starting_index + ending_index)//2

        # If the middle value matches the target, record it as a potential last occurence
        # Continue searching to the right side of the list to check for later occurences
        if values [middle_index] == target:
            last_occurence = middle_index
            starting_index = middle_index + 1 

        # If the middle value is less than the target, move right to search larger values 
        elif values [middle_index] < target:
            starting_index = middle_index + 1 

        # If the middle value is greater than the target, move left to search smaller values
        else: 
            ending_index = middle_index - 1

    # Compute total count of targets if both first and last indicies exist
    total_target_count = 0
    if first_occurence != -1 and last_occurence != -1:

        # Calculate the total number of elements between start and end indicies (inclusive)
        total_target_count = last_occurence - first_occurence + 1

    # Return the total count of the target value in the list
    return total_target_count

def test_occurences ():
    """ 
    Run a set of case to verify the occurences() function. 
    
    Test the occurences() function with various cases to ensure correctness.
    Each test prints the expected and actual results for verification code runs without error.
    """

    # Case 1: Target value is appears multiple times in the middle of list 
    values = [1,2,2,3,4,5]
    target = 2 
    print("Expected occurence: 2")
    print("Actual occurence:", occurences(values, target))
    print()

    # Case 2: One target occurences at the start 
    values = [1,2,3,4,5,6,7]
    target = 1
    print("Expected occurence: 1")
    print("Actual occurence:", occurences(values, target))
    print()

    # Case 3: One target occurences at the end 
    values = [1,2,3,4,5,6,7]
    target = 7
    print("Expected occurence: 1")
    print("Actual occurence:", occurences(values, target))
    print()

    # Case 4: All values in the list are the target value
    values = [1,1,1,1,1,1,1,1,1,1,1,1]
    target = 1
    print("Expected occurence: 12")
    print("Actual occurence:", occurences(values, target))
    print()

    # Case 5: No target occurences in list
    values = [1,2,3,4,5,5,8,7]
    target = 6
    print("Expected: 0")
    print("Actual:", occurences(values, target))
    print()

# Run test
test_occurences()











