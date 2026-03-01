class graph:
    """
    Represent an undirected weighted graph using an adjacency matrix.

    Attributes:
        __n (int): Number of vertices in the graph.
        __G (list of list of int): Adjacency matrix representing the graph.
        Default_graph_size (int): Default size of the graph if not specified.
        __G[i][j] = weight of edge between vertex i and vertex j, 0 if no edge exists.
    
    """

    Default_graph_size = 4
    Double_count_correction = 2

    def __init__(self, n = Default_graph_size) -> None:
        """
        Initialize a graph with a given number of vertices.

        Parameters:
            n (int): Number of vertices in the graph. Default is Default_graph_size.    
        
        """
        # Set number of vertices
        self.__n = n
        # Initialize adjacency matrix with zeros
        self.__G = [[0 for _ in range(n)] for _ in range(n)]

    def _edge_counter (self) -> int:
        """
        Count the number of edges in the graph.
        Return:
            int: Number of edges in the graph.
        """
        # Initialize edge count and begin with the first row (vertex i)
        edge_count = 0 
        i = 0 

        # Iterate over each vertex (row in adjacency matrix)
        while i < self.__n:
            j = 0
            # Iterate over each vertex (column in adjacency matrix)
            while j < self.__n:
                # If an edge exists between vertex i and vertex j, increment the count
                if self.__G[i][j] != 0:
                    edge_count += 1
                # Move to the next column and row 
                j += 1
            i += 1
        # Each edge is counted twice in an undirected graph, so divide by 2 
        return edge_count // self.Double_count_correction 
    
    def _edge_weights(self) -> tuple[None | int, None | int]:
        """
        Find the shortest and longest edge weights in the graph.
        Return:
            tuple: (smallest_weight, largest_weight) or (None, None) if no edges exist.
        """
        # Initialize variables to track smallest and largest edge weights 
        smallest_weight = None
        largest_weight = None

        # Start with the first row (vertex i)
        i = 0
        # Iterate over each vertex (row in adjacency matrix)
        while i < self.__n:
            # Start with column index greater than i 
            j = i + 1 

            # Loop over remaining columns 
            while j < self.__n:
                # Get the weight of the edge between vertex i and vertex j
                weight = self.__G[i][j]

                # If an edge exists update smallest and largest weights accordingly
                if weight != 0: 
                    # Update smallest weight if it is None or current weight is smaller
                    if smallest_weight is None or weight < smallest_weight:
                        smallest_weight = weight
                    # Update largest weight if it is None or current weight is larger
                    if largest_weight is None or weight > largest_weight:
                        largest_weight = weight
                # Move to the next column and row 
                j += 1
            i += 1
        # Return the smallest and largest edge weights found
        return (smallest_weight, largest_weight)
    
    def add_edge(self, u: int, v: int, weight: int) -> None:
        """
        Add an undirected edge of given weight between vertices u and v.

        Parameters:
            u (int): Index of the first vertex.
            v (int): Index of the second vertex.
            weight (int): Weight of the edge.

        Weight must be non negative.
        """
        # Do not add edge if weight is not positive
        if weight <= 0:
            return 
        # Add the edge in adjacency matrix for undirected graph
        self.__G[u][v] = weight 
        self.__G[v][u] = weight

    def adjust_edge(self, u: int, v: int, new_weight: int) -> None:
        """
        Adjust the weight of an existing edge.

        Parameters:
            u (int): Index of the first vertex.
            v (int): Index of the second vertex.
            new_weight (int): New weight of the edge.

        If edge does not exist do nothing.
        """
        # Check if edge exists and new weight is non negative and update weight
        if self.__G[u][v] != 0 and new_weight >= 0:
            self.__G[u][v] = new_weight
            self.__G[v][u] = new_weight  

    def remove_edge(self, u: int, v: int) -> None:
        """
        Remove an edge between u and v.

        Parameters:
            u (int): Index of the first vertex.
            v (int): Index of the second vertex.    
        """  
        # Set the weight of the edge to 0 to remove it
        self.__G[u][v] = 0
        self.__G[v][u] = 0

    def exists_edge(self, u: int, v: int) -> bool:
        """
        Check if an edge exists between u and v.

        Parameters:
            u (int): Index of the first vertex.
            v (int): Index of the second vertex.
        Return:
            bool: True if edge exists, False otherwise.
        """
        # Return True if weight is not 0, indicating an edge exists
        return self.__G[u][v] != 0
    
    def find_popular(self) -> int:
        """
        Find the index of the vertex with the most neighbors.

        Return:
            int: Index of the vertex with the most neighbors.
        """
        # Initialize variables to track the vertex with the most neighbors
        best_index = 0
        # Number of edges touching that vertex
        best_edges_degree = -1

        # Loop over all vertices
        i = 0 
        while i < self.__n:

            # Initialize count of edges for current vertex
            current_edges_degree = 0
            j = 0
            while j < self.__n:
                # If an edge exists between vertex i and vertex j, increment the degree count
                if self.__G[i][j] != 0:
                    current_edges_degree += 1
                # Move to the next column
                j += 1
            # Update best index if current vertex has more edges
            if current_edges_degree > best_edges_degree:
                best_edges_degree = current_edges_degree
                best_index = i
            # Move to the next row
            i += 1
        
        # Return the index of the vertex with the most neighbors
        return best_index
    
    def describe(self) -> None:
        """
        Print the number of vertices, edges, shortest and longest edge weights.
        """
        # Count total edges in graph and find shortest and longest edges
        count = self._edge_counter()
        (shortest, longest) = self._edge_weights()

        # Print the graph summary
        print("Verticies" , self.__n)
        print("Edges:", count)
        print("Shortest edge:" , shortest)
        print ("Longest edge:" , longest)

    def __str__(self) -> str:
        """
        String representation of the aproperties of the adjacency matrix graph 
        Return:
            str: Formatted string with number of vertices, edges, shortest and longest edge weights.
        """
        # Count total edges in graph and find shortest and longest edges
        count = self._edge_counter()
        (shortest, longest) = self._edge_weights()

        # Construct the formatted string
        str1 = "Verticies: " + str(self.__n) 
        str2 = "Edges: " + str(count)
        str3 = "Shortest edge: " + str(shortest)
        str4 = "Longest edge: " + str(longest)

        # Return the combined string
        return str1 + "\n" + str2 + "\n" + str3 + "\n" + str4
    
# Test cases 
if __name__ == "__main__":
    
    # Test case for default graph size
    g = graph()
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 3)
    g.add_edge(1, 2, 1)
    g.add_edge(1, 3, 2)
    print(g)
    popular_vertex = g.find_popular()
    print(f"Vertex with most neighbors: {popular_vertex}")
    print("\n")

    # Test case for custom graph size 7
    g = graph(7)
    g.add_edge(0, 3, 10)
    g.add_edge(0, 6, 5)
    g.add_edge(1, 2, 2)
    g.add_edge(3, 4, 8)
    print(g)
    print("\n")

    # Test case for removing an edge
    g2 = graph(5)
    g2.add_edge(0, 1, 7)
    g2.add_edge(1, 2, 4)
    print("Before removing edge:")
    g2.describe()
    print("\n")
    g2.remove_edge(0, 1)
    print ("After removing edge:")
    g2.describe()
    print("\n")

    # Graph with no edges 
    g = graph(3)
    g.describe()
    print("\n")

    # Invalid edge weight test
    g = graph(4)
    g.add_edge(0, 1, -5)  
    g.add_edge(1, 2, 0)   
    g.describe()