from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class Node:
    """
    A node in the graph.
    
    Attributes:
        name (str): The name of the city.
        edges (Dict[str, int]): A dictionary of the cities that can be reached from the current city and the cost to get to that city.
    """
    name: str = field(default_factory=str)
    
    # String is the city, int is the cost to get to that city from the current city
    edges: Dict[str, int] = field(default_factory=dict)

@dataclass
class Graph:
    """
    A graph of cities and their connections.
    
    Attributes:
        nodes (List[Node]): A list of nodes in the graph.
    """
    nodes: List[Node] = field(default_factory=list)
    
class GraphPath:
    """
    A graph of cities and their connections.
    
    Attributes:
        cities (List[str]): A list of cities in the graph.
        graph (Graph): A graph of cities and their connections.
        
    methods:
        _initialize_graph(self, graph: Graph) -> None: Initializes the graph with the cities and their connections.
        get_graph(self) -> Graph: Returns the graph.
        get_costs_dict_for_city(self, city: str) -> Dict[str, int]: Returns a dictionary of the cities that can be reached from the current city and the cost to get to that city.
        get_cities_list(self) -> List[str]: Returns a list of the cities in the graph.
    """
    def __init__(self):
        """
        Initializes the graph with the cities and their connections.
        
        Args:
            None
        """
        self.cities = [
            'Buffalo',
            'Boston',
            'Pittsburgh',
            'New York',
            'Philadelphia',
            'Baltimore',
            'Salisbury',
            'Washington DC',
            'Richmond',
            'Norfolk',
        ]
        self.graph = Graph()
        self._initialize_graph(self.graph)
    
    def _initialize_graph(self, graph: Graph):
        """
        Initializes the graph with the cities and their connections.
        
        Args:
            graph (Graph): A graph of cities and their connections.
        """
        for city in self.cities:
            node = Node(city, self.get_costs_dict_for_city(city))
            graph.nodes.append(node)
            
    def get_graph(self) -> Graph:
        """
        Returns the graph.
        
        Args:
            None
            
        Returns:
            Graph: A graph of cities and their connections.
        """
        return self.graph
    
    def get_costs_dict_for_city(self, city: str) -> Dict[str, int]:
        """
        Returns a dictionary of the cities that can be reached from the current city and the cost to get to that city.
        
        Args:
            city (str): The city to get the costs for.
            
        Returns:
            Dict[str, int]: A dictionary of the cities that can be reached from the current city and the cost to get to that city.
        """
        if city == 'Buffalo':
            return {
                'Boston': 450,
                'Pittsburgh': 219,
            }
        elif city == 'Boston':
            return {
                'Buffalo': 450,
                'New York': 216,
            }
        elif city == 'Pittsburgh':
            return {
                'Buffalo': 219,
                'New York': 370,
                'Philadelphia': 304,
                'Baltimore': 248,
            }
        elif city == 'New York':
            return {
                'Boston': 216,
                'Pittsburgh': 370,
                'Philadelphia': 94,
            }
        elif city == 'Philadelphia':
            return {
                'Pittsburgh': 304,
                'Baltimore': 101,
                'New York': 94,
                'Salisbury': 138,
            }
        elif city == 'Baltimore':
            return {
                'Pittsburgh': 248,
                'Philadelphia': 101,
                'Salisbury': 117,
                'Washington DC': 45,
            }
        elif city == 'Salisbury':
            return {
                'Baltimore': 117,
                'Washington DC': 116,
                'Philadelphia': 138,
                'Norfolk': 132,
            }
        elif city == 'Washington DC':
            return {
                'Baltimore': 45,
                'Salisbury': 116,
                'Richmond': 110,
            }
        elif city == 'Richmond':
            return {
                'Washington DC': 110,
                'Norfolk': 93,
            }
        elif city == 'Norfolk':
            return {
                'Richmond': 93,
                'Salisbury': 132,
            }
            
    def get_cities_list(self) -> List[str]:
        """
        Returns a list of the cities in the graph.
        
        Args:
            None
            
        Returns:
            List[str]: A list of the cities in the graph.
        """
        return self.cities
        

if __name__ == '__main__':
    graph_path = GraphPath()
    graph = graph_path.get_graph()
    print(graph)
    


