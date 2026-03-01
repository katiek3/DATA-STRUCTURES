class TwoDimensionalQ:
    """
    A model of a two-dimential queue using a circular buffer. 
    The queue tracks front and back positions using row-major order 
    maintaining invarians for a queue withoug physical shifting.

    """
    def __init__(self, n: int = 4):
        """
        Initialize the two-dimensional queue with an n x n array.
        """
        self._underlying: list[list[str]] = [[None for _ in range(n)] for _ in range(n)] # Create an n x n 2D grid filled with None to represent empty queue positions.
        self._n: int = n #Store the grid size. 
        self._capacity: int = n * n #The total capacity of the queue.
        self._usage: int = 0 #The current number of elements in the queue. 
        self._front_row: int = 0 #The row index of the front of the queue.
        self._front_col: int = 0 #The column index of the front of the queue.
        self._back_row: int = 0 #The row index of the back of the queue.
        self._back_col: int = 0 #The column index of the back of the queue.

#Private method to advance the index in row-major order.
    def _advancing_index(self,row: int, col: int) -> tuple[int,int]:
        """
        Advance one position forward in row-major order. 
        Wrap around to the beginning once the end of the array is reached.

        """
        following_col: int = (col +1) % self._n #Handles end of a row
        following_row: int = row #Start with the same row. 
        if following_col == 0: #If the column wrapped around move to the next row.
            following_row = (row +1) % self._n #Move to the next row, wraps to the top if last row is finished.
        return following_row, following_col #Returns coordinates of the next cell [row,column].
    
    def enqueue(self, value: str) -> None:
        """
        Someone is joining the queue. 
        Returns False if the queue is full, if not true otherwise.
        
        """
        successful_enqueue: bool = True
        if self._usage == self._capacity: #If the queue is full.
            successful_enqueue = False  #Cannot enqueue.
        else:
            self._underlying[self._back_row][self._back_col] = value #Place the enqueued value at the back row and column. 
            self._back_row, self._back_col = self._advancing_index (self._back_row, self._back_col) #Advance the back pointer to the next cell.
            self._usage += 1 #If there is space in the queue, increase the usage count. 
        return successful_enqueue
    
    def dequeue(self) -> str | None:
        """
        Someone is leaving the queue.
        The front value.
        Return None if the queue is empty.
        How a 2D circular queue removes elements in FIFO order 
        while tracking which cell is the front and how many individuals are in queue.

        """

        dequeued_value: str | None = None #Start with None if queue is empty.
        if self._usage > 0: #Only dequeue if there is something in the queue.
            dequeued_value = self._underlying [self._front_row][self._front_col] #Get the value at the current front position of the queue
            self._underlying[self._front_row][self._front_col] = None #Once they have dequeued, remove the value from the queue. 
            self._front_row, self._front_col = self._advancing_index (self._front_row, self._front_col) #Advance the front pointer to the next cell. 
            self._usage -= 1 #If there was a value to dequeue, decrease the usage count.
        return dequeued_value
    
    def peek(self) -> str | None:
        """
        Return the front value without removing it from the queue.
        Checking which individual is next in line without serving them.
        If the queu is empty result if None.
        """
        peeked_value: str | None = None #Start with None if queue is empty.
        if self._usage > 0: #If the queue is not empty track how many elements are in the queue currently.
            peeked_value = self._underlying[self._front_row] [self._front_col] #Get the value at the front pointer. 
            return peeked_value #Return front pointer value.
        
    def list_queue (self) -> list[str]:
        """
        List all values in the queue from front to back in logcial order.
        Handles wrapping correctly. 

        """
        values_in_queue: list[str] = [] #Begin with an empty list.
        current_row, current_col = self._front_row, self._front_col
        for _ in range(self._usage): #Loop through the number of elements currently in the queue.
            values_in_queue = values_in_queue + [self._underlying[current_row][current_col]] #Add the value at the current position to the list.
            current_row, current_col = self._advancing_index(current_row, current_col) #Advance to the next position.
        return values_in_queue #Return the list of values in the queue.

    def get_capacity(self) -> int:
        """
        Return the maximum number of elements the queue can hold.
        """
        return self._capacity
        
    def get_usage(self) -> int:
        """
        Return the current number of occupied seats in the queue.
        """
        return self._usage

    def __repr__(self) -> str:
        """
        Return a string representation of the queue.
        """
        grid_order = self.list_queue() #Get a list of all elements in the queue.
        grid_display = "" #Initialize an empty string.
        for i in range (self._n): #Loop through each row of the underlying 2D array.
            grid_display += f"Row {i}: {self._underlying[i]}\n"
        return f"TwoDimensionalQ grid = {grid_order}, \n{grid_display}" #Queues logical order (from front to back) and the 2D array representation.

    def __bool__(self) -> bool:
        """
        Return True if the queue is not empty, False otherwise.
        """
        not_empty_queue: bool = self._usage > 0 #The queue is not empty if usage is greater than 0.
        return not_empty_queue #Return True if the queue is not empty, False otherwise.
        

if __name__ == "__main__":
#2X2 Queue Test Case
    q = TwoDimensionalQ(2)
#Enqueue individuals
print("Enqueue Alice:", q.enqueue("Alice"))
print("Enqueue Bob:", q.enqueue("Bob"))
print("Enqueue Cathy:", q.enqueue("Cathy"))
print("Enqueue John:", q.enqueue("John"))
# Show current queue
print("Current Queue:")
print(q)    
#Peek at the front of the queue
print("Peek at front:", q.peek())
#Dequeue individuals
print("Dequeued:", q.dequeue())
print("Current queue after dequeue:")
print(q)

#Peek at the front of the queue
print("Peek at front:", q.peek())
#Dequeue another individual
print("Dequeued:", q.dequeue())
print("Current queue after another dequeue:")
print(q)
   
#empty queue 
print("\n--Emptying the Queue--") 
empty_queue = TwoDimensionalQ(3)
print("Dequeue from empty queue:", empty_queue.dequeue())
print("Peek the empty queue:", empty_queue.peek())
print("Is the queue empty?", not empty_queue)
print("Empty queue:")
print(empty_queue)

