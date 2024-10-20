from dfs_search import DFSSearch
from bfs_search import BFSSearch
from ucs_search import UCSSearch

def run_all_searches():
    """
    Runs all the search algorithms.
    """
    searches = [
        ("Breadth-First Search", BFSSearch()),
        ("Depth-First Search", DFSSearch()),
        ("Uniform Cost Search", UCSSearch())
    ]

    # Get user input once
    # Same start and goal city for all searches
    start_city = searches[0][1].select_city('Select the start city:')
    print()
    goal_city = searches[0][1].select_city('Select the goal city:')

    print("\nRunning all search algorithms...\n")

    for name, search in searches:
        print(f"=== {name} ===")
        
        # Run the search using the algorithm's run_search method with pre-selected cities
        search.run_search(start_city, goal_city)
        
        print()

if __name__ == "__main__":
    run_all_searches()