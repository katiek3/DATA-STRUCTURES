class MyFirstPriorityQueue:
    """
    A maximum-heap based priority queue implementation.
    
    Class maintains a list of elements in a maximum-heap structure, where 
    the largest element is always at the root of the heap. 
    It implements priority queue operations including violation check,
    add, extract, restore, and peek. 

    Helper methods such as restoring the heap and calculating parent/child indicies 
    help maintain heap properties.

    """
    # Constants to avoid magic numbers 
    _CHILD_MULTIPLIER: int = 2
    _CHILD_INDEX: int = 1
    _CHILD_INDEX_TWO: int = 2

# --- Special Methods ---
    def __init__(self):
        """Initialize an empty priority queue."""
        # The underlying data structure is a list that will be maintained as a heap.
        self._underlying = []

    def __bool__(self) -> bool:
        """Return False when the queue is empty."""
        return len(self._underlying) != 0
    
    def __str__(self) -> str: 
        """A string representation of the queue."""
        return f"MyFirstPriorityQueue({self._underlying})"
    
    def __len__(self) -> int:
        """The number of items in the queue."""
        return len(self._underlying)
    
# --- Helper Methods ---
    def is_empty(self) -> bool:
        """True if the queue is empty."""
        return not self.__bool__()
    
    def size (self) -> int:
        """The number of elements in the array."""
        return self.__len__()
    
 # --- Core functionality ---
    def _parent(self, child: int) -> int:
        """Return the index of the parent of a given child node in the heap array."""
        # Compute parent index using integer division
        return (child - 1) // self._CHILD_MULTIPLIER
    
    def _left(self, parent: int) -> int:
        """Return index of left child of a given parent node in the heap array."""
        return self._CHILD_MULTIPLIER * parent + 1
    
    def _right(self, parent: int) -> int:
        """Return index of right child of a given parent node in the heap array."""
        return self._CHILD_MULTIPLIER * parent + self._CHILD_MULTIPLIER
    
    def _violation_occurs(self, parent: int) -> bool:
        """Check if the maximum-heap property is violated at the parent index."""
        """If the child is larger than the parent, then the violation occurs."""
        # Get the indicies of the left and right children of the parent node
        left_child = self._left(parent)
        right_child = self._right(parent)
        # If the left child exists and is greater than the parent the maximum-heap property is violated
        # If the right child exists and is greater than the parent the maximum-heap property is violated
        # Return True if either child violates the maximum-heap property
        return (left_child < len(self._underlying) and self._underlying[left_child] > self._underlying[parent])or \
                (right_child < len(self._underlying) and self._underlying[right_child] > self._underlying[parent])
    
    def _restore(self,parent: int = 0) -> int:
        """Restore the heap property at the given parent index."""
        while True:
            # Calculate the indicies of the left and right children
            left_child = self._left(parent)
            right_child = self._right(parent)
            # Asuume the parent node is the largest
            largest_value = parent 

            # Check if the left child exists and its index is within the list bounds
            if left_child < len(self._underlying):
                # Compare the value of the left child with the current largest value 
                if self._underlying[left_child] > self._underlying[largest_value]:
                    # If the left child is greater, update the 'largest' to point to the left 
                    largest_value = left_child
        
            # Check if the right child exists and its index is within the list bounds
            if right_child < len(self._underlying):
                # Compare the value of the right child with the current largest value 
                if self._underlying[right_child] > self._underlying[largest_value]:
                    # If the right child is greater, update the largest_value to point to the right
                    largest_value = right_child

            # If the largest nodes is not the parent, it means a child was larger
            # Swap the parent with that child to fix heap property
            if largest_value != parent:
                # Swap parent with largest child
                self._underlying[parent], self._underlying[largest_value] = (
                    self._underlying[largest_value], self._underlying[parent]
            )
            # New index that now contains the original parent value
            return largest_value

    def add (self, value: int) -> None:
        """
        Add a new value to the priority queue.
        Public as it is a core operation of any priority queue.
        """
        # Append the new value to the end of the underlying list
        self._underlying.append(value)

        # Start at the index of the newly added element
        last_index = len(self._underlying) - 1

        # Shift the new data up the heap until the proprty is restored
        while last_index >0:
            # Find the index of the parent node 
            parent_index = self._parent(last_index)

            # If the new value is greater than the parent value, swap them 
            if self._underlying[last_index] > self._underlying[parent_index]:
                self._underlying[last_index], self._underlying[parent_index] = (
                    self._underlying[parent_index], self._underlying[last_index]

                )
                # Move up to the parent index and continue checking
                last_index = parent_index
            else:
                # If the heap property is satisfied, stop shifting data
                last_index = 0

        # return none if no elements in the array 
        return None                

    def extract_most_important (self) -> int:
        """
        Remove and return the most important element.
        Public so users can get the max from the queue.
        """
        # Initialize the return value
        value_to_return = None

        # Continue on if the heap is not empty
        if len(self._underlying) > 0:
            # Store the root value (most important value) to return it 
            value_to_return = self._underlying[0]

            # Take the last element in the heap
            last_value = self._underlying[len(self._underlying) - 1] 

            # Remove the last element from the heap by creating a new list with it
            new_underlying = []
            for i in range(len(self._underlying) - 1):
                new_underlying.append(self._underlying[i])
            self._underlying = new_underlying

            # Put last element at the root if heap is not empty
            if len(self._underlying) > 0:
                self._underlying[0] = last_value
                # Restore the heap property by shifting the new root down
                self._restore()
        # Return most important element 
        return value_to_return 
    
    def peek(self) -> int:
        """
        The most important element (max-heap) without removing it.
        Public for safe inspection of the queue.
        """
        # There is no elemnents in the list, return None
        if len(self._underlying) == 0:
            peeked_value = None
        else: 
            # There are elements in the list, the most important element is at the root of the heap
            peeked_value = self._underlying[0]
        
        # Return the value of the root without removing it
        return peeked_value
    
    def peek_next (self) -> int: 
        """
        Return the second most important element in the maximum heap without removing it.
        
        For a maximum-heap, the largest element is at the root (index 0). The second largest
        element is one of the children of the parent (at index 1 or 2, if they exist). 
        Return None if the heap has fewer than 2 elements.

        Public for optional inspection for the second important value.
        """
        # If the heap has 0 or 1 elements, there is no second largest element
        if len(self._underlying) <= 1: 
            peeked_next_value = None
        # If the heap has exactly 2 elements, the second element is at index 1
        elif len(self._underlying) == self._CHILD_MULTIPLIER:
            peeked_next_value = self._underlying[self._CHILD_INDEX]
        else:
            # Compare the two children of the root to find second largest value in array
            left = self._underlying[self._CHILD_INDEX]
            right = self._underlying[self._CHILD_INDEX_TWO]
            if left > right:
                peeked_next_value = left 
            else: 
                peeked_next_value = right

        # Return the second largest value without removing it 
        return peeked_next_value
    
    

if __name__ == "__main__": 
    pq = MyFirstPriorityQueue()

    # Add elements to the list
    pq.add(10)
    pq.add(12)
    pq.add(1)
    pq.add(50)
    pq.add(5)
    pq.add(30)
    pq.add(20)
    # Present heapped list
    print("Heap after adding element:",pq)

    # Peek the most important element
    print ("Peek:", pq.peek())
    print(pq)


    # Peek next most important element
    print("Peek next important:", pq.peek_next())

    # Peek an empty queue
    empty_queue = MyFirstPriorityQueue()
    print("Empty queue peek:", empty_queue.peek())
    print("Empty queue next peek:", empty_queue.peek_next())


    # Extract the most important and show new heap after 
    print("Extracted most important:", pq.extract_most_important())
    print("Heap after extraction:", pq)
    print("Extract next important:", pq.extract_most_important())
    print("Heap after next extraction:", pq)

    # Restore heap 
    pq._underlying = [11,13,6,70,3,5,8]
    print("Before restore:",pq)

    #Restore heap starting from the top manually
    pq._restore(1)
    print("After restoring:",pq)
    pq._restore()
    print("After restoring from the top:",pq)
    pq._restore(1)
    print("After restoring:",pq)


    # Check heap size and if it is empty
    print("Heap size:", pq.size())
    print("Is the queue empty?:", pq.is_empty())



    







