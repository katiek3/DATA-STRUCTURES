from Node import Node

class DoublyLinkedList:

    def __init__(self):
        #Initialize an empty list with no head, tail, or size.
        self.__head = None
        self.__tail = None
        self.__size = 0

    def __str__(self):
        #Return string version of the list (call __repr__).
        return self.__repr__()

    def __repr__(self):
        #Build a readable string showing all nodes linked together. 
        nodes = []
        current = self.__head
        while current is not None:
            nodes.append(str(current))
            current = current.get_next()
        return " <-> ".join(nodes)

    def is_empty(self):
        #Return True if list has no elements.
        return self.__size == 0

    def get_size(self):
        #Return number of nodes in list.
        return self.__size

    def add_to_back(self, data):
        #Add new node to end of list. 
        new_node = Node(data)
        if self.is_empty():
            #If list is empty, new node becomes the head.
            self.__head = new_node
        else:
            #Link the new node to current tail.
            new_node.set_prev(self.__tail)
            self.__tail.set_next(new_node)
        #Update tail reference.
        self.__tail = new_node
        #Increase list size by one.
        self.__size += 1
    
    def add_to_front(self, data):
        #Add a new node to front of list.
        new_node = Node(data)
        if self.is_empty():
            #If list is empty, new node is the tail.
            self.__tail = new_node
        else:
            #Link new node to current head. 
            new_node.set_next(self.__head)
            self.__head.set_prev(new_node)
        #Update head reference.
        self.__head = new_node
        #Increase list size by one
        self.__size += 1

   #Middle of a double linked list
    def find_middle(self) -> None | Node: 
        """
        Find the middle of a simple linked list. 
        Find the middle of a double linked list, with pointers that move at the same speed. 
        One node at a time. 
        (n+1)-th node as the middle node.
        """
        middle = None #Initialize middle to None.
        index = 2
        if not self.is_empty(): #Check if the list is not empty. Return None if condition fails.
            middle_index = self.__size // index #Calculate the index of the middle node using integer division. Even number of nodes gives the second of the two middles. Odd number of nodes gives the true middle. 
            current = self.__head #Start from the head of the list.
            for i in range (middle_index): #Loop will iterate middle_index times from head toward the middle.
                current = current.get_next() #Move to the next node in each iteration. Move current one step forward.
            middle = current #once middle is reached, store in variable middle. 
        return middle #Return the middle node or None if the list is empty. 
    
    #Detect a Loop
    def has_loop(self) -> bool:
        """
        Tell if a simple (single) linked list has a loop.
        Two pointers traversing the list at different speeds. 
        One pointer twice as faster as the other. 
        If there is a loop the pointers eventually will meet. 
        If there is no loop, the faster pointer will reach the end of the list without meeting the other. 
        """
        #Check if the list has at least one node (there is a head node).
        #Check if the first node's previous pointer points to something.
        #Both conditions above must be true for this to be true. 
        
        #Check if the list has at least one node. 
        #Check if last node's next pointer points to something. 
        #Only counts if a tail actually exists 
        loop = ((self.__head is not None and self.__head.get_prev() is not None) 
                or #Either the head's previous is not None or the tail's next is not None then loop is true. 
        (self.__tail is not None and self.__tail.get_next()is not None))
        return loop 
    
    #Detect a gap
    def _has_gap_forward(self) -> bool:
        """
        Check if there is a gap (broken link) in the forward direction of doubly linked list.
        Links between two consecutive nodes do not correctly point to each other. 

        """
        gap_present = False #Set variable gap_present to False assuming there is no gaps.
        current = self.__head #Start at the first node (head) of the list.
        while current and current.get_next() and not gap_present: #Keep looping while there is a current node (head), node has a next node, and you haven't already found a gap.
            if current.get_next().get_prev() != current: #Check if connection bewteen two nodes is broken. 
                gap_present = True #True if forward link and backward link are out of sync. Gap exists.
            current = current.get_next() #Move to the next node until you find gap or reach end. 
        return gap_present #If no gaps found, gap_present stays False. If gap found, return True.
    
    def _has_gap_backward(self) -> bool:
        """
        Check if there is a gap (broken list) in the backwards direction of doubly linked list.
        Links between two consecutive nodes do not correctly point to each other when moving backward.
        
        """
        gap_present = False #Set variable gap_present to False, assuming there is no gaps. 
        current = self.__tail #Start at the last node (tail) of the list.
        while current and current.get_prev() and not gap_present: #Keep looping while there is a current node (tail), a previous node, and no gap is found. 
            if current.get_prev().get_next() != current: #Check if connection between two nodes is broken. If the next node is not the same as current, then there is a gap.
                gap_present = True #Turn Boolean value to true if the pointer at the node that comes before current does not point back to current. There is a gap.
            current = current.get_prev() #Move to back to previous node.
        return gap_present #If no gaps found, gap_present stays False. If gap found, return True.
    
    def has_gap_(self) -> bool: 
        """
        Return True if the DoublelyLinkedList object has a gap either 
        in the forward or the backwards direction and False otherwise. 

        """
        #Check forward gaps from head to tail using helper method _has_gap_forward(). If a gap in the forward direction return True. Otherwise False.  
        #Check bakward gaps from tail to hea using helper method _has_gap_backward(). If a gap in the backward direction return True. Otherwise False. 
        #If the first value is True stop and return true if not, check second value. 
        gap_present = self.has_gap_forward() or self._has_gap_backward()
        return gap_present #Return Boolean value. 
        
    #---Simple Test Cases---#
if __name__ == "__main__":

    #Test empty list
    dubll = DoublyLinkedList()
    print("List is empty?", dubll.is_empty())
    print("Size:", dubll.get_size())
    print("List contents:", dubll)
    print()

    #Add elemts to list
    dubll.add_to_back("A")
    dubll.add_to_back("B")
    dubll.add_to_back("C")
    dubll.add_to_back("D")
    dubll.add_to_back("E")
    print("List contenst", dubll)

    #Chek for gaps
    print("Has gap forward?", dubll._has_gap_forward())
    print("Has gap backward", dubll._has_gap_backward())

    #Break A-> B connection
    nodeA = dubll._DoublyLinkedList__head
    nodeB = nodeA.get_next()
    nodeC = nodeB.get_next()
    nodeB.set_prev(nodeC) #Break backward link of nodeB (gap)
   
    #Check gaps
    print("Forward gap?", dubll._has_gap_forward())
    print("Backward gap?", dubll._has_gap_backward())


    



        


            