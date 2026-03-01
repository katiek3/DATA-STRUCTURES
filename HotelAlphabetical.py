# UPDATED: Oct 16 Added self._size = 0 in `_rehash`
from Guest import Guest    # UPDATED: Oct 15

class HotelAlphabetical:
    """Class representing a hotel where guests are stored in rooms based on
    the first initial of their names. Each room is a linked list of guests.
    """

    _DEFAULT_CAPACITY = 26
    _ASCII_LEFT_EDGE = ord("A")
    _ASCII_RIGHT_EDGE = ord("Z")
    _EMPTY = "boohoo, your hotel is empty."
    _NEXT_GUEST = " --> "

    _LOAD_FACTOR_THRESHOLD = 0.7
    _INCREMENT_FACTOR = 2

    def __init__(self, capacity: int = _DEFAULT_CAPACITY):
        self._capacity = capacity
        self._hotel = [None] * capacity  # Array of linked lists for each letter
        self._usage = 0  # number of array slots used
        self._size = 0

    def _get_index(self, name: str) -> int:
        """Compute the index in the hotel array based on the first
        initial of the guest's name."""
        # Default to 0 if name is None or empty or not A-Z
        room_index = 0
        if name is not None and len(name) > 0:
            # DISCUSSION POINT: should we be computing the first initial
            # here or should it be done in object Guest?
            initial_ascii = ord(name.upper()[0])
            if self._ASCII_LEFT_EDGE <= initial_ascii <= self._ASCII_RIGHT_EDGE:
                room_index = initial_ascii % self._capacity
        return room_index

    def _check_load_factor(self) -> bool:
        """Check if the load factor exceeds the threshold."""
        load_factor = self._usage / self._capacity
        return load_factor > self._LOAD_FACTOR_THRESHOLD

    def _rehash(self) -> None:
        """Rehash the hotel by increasing its capacity and reassigning guests."""
        # Preserve the old hotel array and its capacity
        old_hotel = self._hotel
        old_capacity = self._capacity
        # Create a new hotel array with increased capacity
        self._capacity *= self._INCREMENT_FACTOR
        # Initialize the new hotel array and reset usage
        self._hotel = [None] * self._capacity
        self._usage = 0
        self._size = 0       # UPDATE Oct 16
        # Reinsert all guests into the new hotel array
        for room in range(old_capacity):
            guest_in_room = old_hotel[room]
            while guest_in_room is not None:
                self.add_guest(guest_in_room.get_name())
                guest_in_room = guest_in_room.get_next()

    def add_guest(self, name: str) -> None:
        """Add a guest to the hotel."""
        if self._check_load_factor():
            self._rehash()
        # Compute the room index based on the first initial of the name
        room = self._get_index(name)
        # Create a new guest object
        guest = Guest(name)
        # Insert the guest at the front of the linked list for that room
        if self._hotel[room] is None:
            self._hotel[room] = guest
            self._usage += 1
        else:
            guest.set_next(self._hotel[room])
            self._hotel[room] = guest
        # Increment the current occupancy of the hotel
        self._size += 1

    def guest_exists (self, guest_name: str) -> bool:
        """
        Check whether a guest with the given name guest_name is current in the hotel.
        If guest is found, return True.
        If guest is not found, return False.
        """
        #Initialize variables.
        guest_found = False #Set to False at the start
        room_index = self._get_index(guest_name) #Determine which room index the guest should be based on their first initial
        room_first_guest = self._hotel[room_index] #First guest stored in the hotel room

        #Loop through the linked list of guests in that room 
        #Continues until no more guests found
        while room_first_guest != None:
            #If current guests matches one looking for return True
            if room_first_guest.get_name() == guest_name: 
                guest_found = True
            #Move to the next guest in the linked list and repeat 
            room_first_guest = room_first_guest.get_next()
        #Return True if the guest was found, False otherwise
        return guest_found
    
    def remove_guest (self, guest_name:str) -> Guest | None: 
        """
        Remove guest, if present, from the hotel.
        If removal successful, the guest object is returned; otherwise return None.
        """
        #Initialize return value 
        removed_guest = None

        #Determine the room they are in 
        room_occupied = self._get_index(guest_name)

        #Begin at first guest stored in the hotel room
        guest_node = self._hotel[room_occupied] 
        previous_guest = None

        #Itterate through linked list to find matching guest to remove
        while guest_node != None:
            #If a match is found, remove from linked list
            if guest_node.get_name() == guest_name:
                removed_guest = guest_node
                #If guest is the first in the room 
                if previous_guest == None: #Check if guest to remove is first in the line
                    self._hotel[room_occupied] = guest_node.get_next() #Move head pointer forward, removing the first guest from the linked list
                    #If the room is empty after removal decrease usage of room by 1
                    if self._hotel[room_occupied] == None:
                        self._usage -= 1
                #If guest if not the first in the room 
                #Update pointer to the node after the one being deleted
                else:
                    previous_guest.set_next(guest_node.get_next())
                #Decrease total count of guests in hotel by 1
                #Move to the next guest in list
                self._size -= 1 
                guest_node = None
            #If the current guest is not the target move to the next guest
            else:
                previous_guest = guest_node
                guest_node = guest_node.get_next()
        #Return guest that was removed
        return removed_guest
        

    def __repr__(self) -> str:
        hotel_string = self._EMPTY
        if self._size > 0:
            hotel_string = f"\nThere are {self._size} guest(s) in your hotel."
            hotel_string += f"\nThe hotel has a capacity of {self._capacity} rooms."
            hotel_string += f" and is using {self._usage} room(s)."
            hotel_string += f"\nThe load factor is {self._usage/self._capacity:.2f}."
            hotel_string += f" The {self._size} guest(s) are:"
            for room in range(self._capacity):
                if self._hotel[room] is not None:
                    hotel_string += f"\n\tRoom {room:02d}: "
                    guest_in_room = self._hotel[room]
                    while guest_in_room is not None:
                        hotel_string += f"{guest_in_room.get_name()}{self._NEXT_GUEST}"
                        guest_in_room = guest_in_room.get_next()
                    hotel_string += ""
        return hotel_string
    
#Test cases
hotel = HotelAlphabetical()
hotel.add_guest("Alice")
hotel.add_guest("Bob")
hotel.add_guest("Dan")
hotel.add_guest("Sage")
hotel.add_guest("Silver")
hotel.add_guest("Abby")
print (hotel)

#Guest exists test case
print("Bob exists:", hotel.guest_exists("Bob")) 
print("Alice exists:", hotel.guest_exists("Alice")) 
print("Calvin exists:", hotel.guest_exists("Calvin")) 

#Remove guest test case
removed = hotel.remove_guest("Silver")
print("Silver removed:", removed.get_name())
print("Silver still in hotel?:", hotel.guest_exists("Silver"))
print (hotel)

#Multiple guests test case
hotel.add_guest("Billy")
hotel.add_guest("Bobby")
hotel.add_guest("Ben")
hotel.add_guest("Bush")
print(hotel)                                        
removed = hotel.remove_guest("Ben")
print("Removed:", removed.get_name())
print (hotel)

#Case testing 
hotel.add_guest("AideN")
hotel.add_guest("ADAM")
print (hotel)
print("Aiden exists:", hotel.guest_exists("Aiden")) 
print("AideN exists:", hotel.guest_exists("AideN")) 
