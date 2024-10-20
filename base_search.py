from abc import ABC, abstractmethod
import time
from typing import List, Tuple, Optional, Any
from graph import GraphPath, Graph

class GraphSearch(ABC):
    """
    Base class for graph search algorithms.
    
    Implements various helper methods to be used by all search algorithms:
        - find_node_by_name: Finds a node by its name.
        - select_city: Prompts the user to select a city from a list of cities.
        - run_search: Runs the search algorithm with user input for start and goal cities.
    
    It defines an abstract method for the search algorithm to be implemented by the subclass:
        - search: The main search method that must be implemented by the subclass.
        
    Attributes:
        graph_path (GraphPath): A graph path object.
        graph (Graph): A graph object.
        cities (List[str]): A list of the cities in the graph.
    
    Methods:
        create_graph_path: Creates a graph path object.
        find_node_by_name: Finds a node by its name.
        select_city: Prompts the user to select a city from a list of cities.
        run_search: Runs the search algorithm with user input for start and goal cities.
        search: The main search method that must be implemented by the subclass.
    """
    def __init__(self):
        self.graph_path: GraphPath = self.create_graph_path()
        self.graph: Graph = self.graph_path.get_graph()
        self.cities: List[str] = self.graph_path.get_cities_list()

    @staticmethod
    def create_graph_path() -> GraphPath:
        """
        Creates a graph path object.
        
        Args:
            None
        
        Returns:
            GraphPath: A graph path object.
        """
        return GraphPath()

    def find_node_by_name(self, node_name: str) -> Optional[Any]:
        """
        Finds a node by its name.
        
        Args:
            node_name (str): The name of the node to find.
        
        Returns:
            Optional[Any]: The node if found, otherwise None.
        """
        for node in self.graph.nodes:
            if node.name == node_name:
                return node
        return None

    def select_city(self, prompt: str) -> str:
        """
        Prompts the user to select a city from a list of cities.
        
        Args:
            prompt (str): The prompt to display to the user.
        
        Returns:
            str: The selected city.
        
        Raises:
            ValueError: If the user enters an invalid choice such as a letter.
        
        Prevent against user input errors such as letters, both numbers being entered at the same time, out of range numbers, etc.
        """
        print(prompt)
        for i, city in enumerate(self.cities, 1):
            print(f"{i}. {city}")
        while True:
            try:
                choice = int(input("Enter the number of your choice: "))
                if 1 <= choice <= len(self.cities):
                    return self.cities[choice - 1]
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a number.")

    @abstractmethod
    def search(self, start: str, goal: str) -> Tuple[Optional[List[str]], int, int, float]:
        """
        Abstract method for the search algorithm to be implemented by the subclass.
        
        Args:
            start (str): The start city.
            goal (str): The goal city.
        
        Returns:
            Tuple[Optional[List[str]], int, int, float]: The path, number of cities visited, total distance, and time taken.
            
        Raises:
            NotImplementedError: If the subclass does not implement the search method.
        """
        raise NotImplementedError("Subclasses must implement the search method.")

    def run_search(self, start_city=None, goal_city=None):
        """
        Runs the search algorithm with given or user input for start and goal cities.
        """
        if start_city is None:
            start_city = self.select_city('Select the start city:')
        if goal_city is None:
            goal_city = self.select_city('Select the goal city:')

        path, cities_visited, total_distance, time_taken = self.search(start_city, goal_city)

        if path:
            print("\n1) Path:", " -> ".join(path))
            print(f"2) Number of cities visited: {cities_visited}")
            print(f"3) Time taken by the algorithm: {time_taken:.8f} seconds")
            print(f"4) Total distance: {total_distance} miles")
        else:
            print(f"No path found between {start_city} and {goal_city}.")
            print(f"Time taken by the algorithm: {time_taken:.8f} seconds")