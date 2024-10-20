from collections import deque
import time
from typing import List, Tuple, Optional, Deque, Set
from base_search import GraphSearch

class BFSSearch(GraphSearch):
    """
    Breadth-First Search implementation.
    
    Methods:
        search: Concrete implementation of the abstract search() method for BFS.
    """
    def search(self, start: str, goal: str) -> Tuple[Optional[List[str]], int, int, float]:
        """
        Concrete implementation of the search() method for BFS.
        
        Args:
            start (str): The start city.
            goal (str): The goal city.
        
        Returns:
            Tuple[Optional[List[str]], int, int, float]: The path, number of cities visited, total distance, and time taken.
            Returns None if no path is found, along with 0 for the number of cities visited, 0 for the total distance, and time taken.
        """
        # Initialize the queue with the start node, its path, and distance
        queue: Deque[Tuple[str, List[str], int]] = deque([(start, [start], 0)])
        # Initialize the visited set with the start node
        visited: Set[str] = set([start])

        # Start timing the search
        start_time = time.time()

        # Process the queue until it's empty
        while queue:
            # Pop the leftmost element from the queue
            (node, path, distance) = queue.popleft()
            
            # If the current node is the goal, return the path, number of cities visited, total distance, and time taken
            if node == goal:
                end_time = time.time()
                return path, len(path) - 1, distance, end_time - start_time
            
            # Find the current node in the graph
            current_node = self.find_node_by_name(node)
            
            # If the current node is not found, continue to the next iteration
            if current_node is None:
                continue

            # Iterate through the current node's neighbors
            for neighbor, cost in current_node.edges.items():
                # If the neighbor has not been visited, add it to the visited set and append to the queue the neighbor with the updated path and distance
                if neighbor not in visited:
                    visited.add(neighbor)
                    new_path = path + [neighbor]
                    new_distance = distance + cost
                    queue.append((neighbor, new_path, new_distance))

        # If no path is found, return None, 0, 0, and the time taken
        end_time = time.time()
        return None, 0, 0, end_time - start_time

if __name__ == "__main__":
    bfs_search = BFSSearch()
    bfs_search.run_search()