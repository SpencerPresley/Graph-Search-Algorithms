import heapq
import time
from typing import List, Tuple, Optional, Set
from base_search import GraphSearch

class UCSSearch(GraphSearch):
    """
    Uniform Cost Search implementation.
    
    Attributes:
        exploration_path (List[str]): A list of the cities explored.
        unique_cities (Set[str]): A set of the cities visited.
    
    Methods:
        search(self, start: str, goal: str) -> Tuple[Optional[List[str]], int, int, float]:
            Concrete implementation of the search() method for UCS.
    """
    def __init__(self):
        """
        Initializes the UCS search.
        
        Calls super().__init__() to initialize the parent class so that the run_search method can be overridden.
        
        Initializes the exploration_path and unique_cities attributes.
        """
        super().__init__()
        self.exploration_path: List[str] = []
        self.unique_cities: Set[str] = set()

    def search(self, start: str, goal: str) -> Tuple[Optional[List[str]], int, int, float]:
        """
        Concrete implementation of the search() method for UCS.
        
        Args:
            start (str): The start city.
            goal (str): The goal city.
            
        Returns:
            Tuple[Optional[List[str]], int, int, float]: The path, number of cities visited, total distance, and time taken.
            
            Returns None if no path is found, along with 0 for the number of cities visited, 0 for the total distance, and time taken.
        """
        # Record the start time
        start_time = time.time()
        
        # Initialize the priority queue with the start node, its path, and cost
        priority_queue = [(0, start, [start])]
        
        # Initialize the unique cities and exploration path
        self.unique_cities = set()
        self.exploration_path = []
        
        # Initialize the total number of explorations
        total_explorations = 0
        
        # Process the priority queue until it's empty
        while priority_queue:
            # Pop the node with the lowest cost from the priority queue
            (cost, node, path) = heapq.heappop(priority_queue)
            
            # Add the node to the exploration path
            self.exploration_path.append(node)
            
            # Increment the total number of explorations
            total_explorations += 1
            
            # If the node has not been visited, add it to the unique cities
            if node not in self.unique_cities:
                self.unique_cities.add(node)
                
                # If the node is the goal, return the path, number of cities visited, total distance, and time taken
                if node == goal:
                    end_time = time.time()
                    return path, total_explorations, cost, end_time - start_time
                
                # Get the current node
                current_node = self.find_node_by_name(node)
                
                # If the current node is not found, continue to the next iteration
                if current_node is None:
                    continue
                
                # Iterate through the neighbors of the current node
                for neighbor, edge_cost in current_node.edges.items():
                    # Calculate the new cost and path
                    new_cost = cost + edge_cost
                    new_path = path + [neighbor]

                    # Push the new node onto the priority queue
                    heapq.heappush(priority_queue, (new_cost, neighbor, new_path))
        
        # If no path is found, record the end time and return None, 
        # total explorations, 0 for the total distance, and time taken
        end_time = time.time()
        return None, total_explorations, 0, end_time - start_time

    def run_search(self, start_city=None, goal_city=None):
        # Call the parent class's run_search method
        super().run_search(start_city, goal_city)
        
        # Additional UCS specific output
        if self.exploration_path:
            print("\n=== Additional Uniform Cost Search Details ===")
            print(f"Total number of city explorations: {len(self.exploration_path)}")
            print(f"Number of unique cities visited: {len(self.unique_cities)}")
            print("\nExploration order:")
            for i, city in enumerate(self.exploration_path, 1):
                print(f"   Step {i}: Explored {city}")

if __name__ == "__main__":
    ucs_search = UCSSearch()
    ucs_search.run_search()