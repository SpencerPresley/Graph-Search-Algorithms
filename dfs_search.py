import time
from typing import List, Tuple, Optional, Set
from base_search import GraphSearch

class DFSSearch(GraphSearch):
    """
    Depth-First Search implementation.
    
    Methods:
        search: Concrete implementation of the abstract search() method for DFS.
    """
    def search(self, start: str, goal: str) -> Tuple[Optional[List[str]], int, int, float]:
        """
        Concrete implementation of the search() method for DFS.
        
        Args:
            start (str): The start city.
            goal (str): The goal city.
        import time
from typing import List, Tuple, Optional, Set
from base_search import GraphSearch

class DFSSearch(GraphSearch):
    """
    Depth-First Search implementation.
    
    Methods:
        search: Concrete implementation of the abstract search() method for DFS.
    """
    def search(self, start: str, goal: str) -> Tuple[Optional[List[str]], int, int, float]:
        """
        Concrete implementation of the search() method for DFS.
        
        Args:
            start (str): The start city.
            goal (str): The goal city.
        
        Returns:
            Tuple[Optional[List[str]], int, int, float]: The path, number of cities visited, total distance, and time taken.
            Returns None if no path is found, along with 0 for the number of cities visited, 0 for the total distance, and time taken.
        """
        # Start timing the search
        start_time = time.time()
        
        # Initialize the stack with the start node, its path, distance, and visited set
        stack: List[Tuple[str, List[str], int, Set[str]]] = [(start, [start], 0, set([start]))]
        
        # Process the stack until it's empty
        while stack:
            # Pop the last element from the stack
            current, path, distance, visited = stack.pop()
            
            # If the current node is the goal, return the path, number of cities visited, total distance, and time taken
            if current == goal:
                end_time = time.time()
                return path, len(path) - 1, distance, end_time - start_time
            
            # Find the current node in the graph
            current_node = self.find_node_by_name(current)
            
            # If the current node is not found, continue to the next iteration
            if current_node is None:
                continue

            # Iterate through the current node's neighbors
            for neighbor, cost in current_node.edges.items():
                # If the neighbor has not been visited, add it to the visited set and append to the stack the neighbor with the updated path and distance
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    new_distance = distance + cost
                    new_visited = visited.copy()
                    new_visited.add(neighbor)
                    stack.append((neighbor, new_path, new_distance, new_visited))
        
        # If no path is found, return None, 0, 0, and the time taken
        end_time = time.time()
        return None, 0, 0, end_time - start_time

if __name__ == "__main__":
    dfs_search = DFSSearch()
    dfs_search.run_search()
        Returns:
            Tuple[Optional[List[str]], int, int, float]: The path, number of cities visited, total distance, and time taken.
            Returns None if no path is found, along with 0 for the number of cities visited, 0 for the total distance, and time taken.
        """
        # Start timing the search
        start_time = time.time()
        
        # Initialize the stack with the start node, its path, distance, and visited set
        stack: List[Tuple[str, List[str], int, Set[str]]] = [(start, [start], 0, set([start]))]
        
        # Process the stack until it's empty
        while stack:
            # Pop the last element from the stack
            current, path, distance, visited = stack.pop()
            
            # If the current node is the goal, return the path, number of cities visited, total distance, and time taken
            if current == goal:
                end_time = time.time()
                return path, len(path) - 1, distance, end_time - start_time
            
            # Find the current node in the graph
            current_node = self.find_node_by_name(current)
            
            # If the current node is not found, continue to the next iteration
            if current_node is None:
                continue

            # Iterate through the current node's neighbors
            for neighbor, cost in current_node.edges.items():
                # If the neighbor has not been visited, add it to the visited set and append to the stack the neighbor with the updated path and distance
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    new_distance = distance + cost
                    new_visited = visited.copy()
                    new_visited.add(neighbor)
                    stack.append((neighbor, new_path, new_distance, new_visited))
        
        # If no path is found, return None, 0, 0, and the time taken
        end_time = time.time()
        return None, 0, 0, end_time - start_time

if __name__ == "__main__":
    dfs_search = DFSSearch()
    dfs_search.run_search()