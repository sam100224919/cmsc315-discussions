"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    TODO (Student):
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track visited nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were visited.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """
    # A missing start node cannot be traversed, so return an empty result.
    if start not in graph:
        return []

    # A FIFO queue makes BFS visit the closest (fewest-edge) nodes first.
    # DFS instead follows one branch deeply before backtracking.
    queue = deque([start])
    visited = {start}  # Mark on enqueue so cycles cannot add a node repeatedly.
    traversal_order = []

    while queue:
        current = queue.popleft()
        traversal_order.append(current)

        # Enqueue each unvisited neighbor. FIFO order processes the graph
        # one distance level at a time.
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal_order


def add_edge(graph, first, second):
    """Add an undirected connection, creating either endpoint if needed."""
    graph.setdefault(first, [])
    graph.setdefault(second, [])

    # Avoid duplicate adjacency entries while keeping the graph undirected.
    if second not in graph[first]:
        graph[first].append(second)
    if first not in graph[second]:
        graph[second].append(first)


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # TODO (Student): CREATE A GRAPH
    # ===============================
    #
    # Requirements:
    # 1. Create a graph using an adjacency list.
    # 2. Include at least 6 nodes.
    # 3. Include multiple connections between nodes.
    # 4. Clearly display the graph structure.
    # 5. Use comments to explain what the nodes and edges represent.

    # Each node represents a movie; an edge connects movies with similar
    # genres, casts, or audience preferences. The graph is undirected.
    graph = {
        "Arrival": ["Interstellar", "Contact"],
        "Interstellar": ["Arrival", "Gravity", "The Martian"],
        "Contact": ["Arrival", "Hidden Figures"],
        "Gravity": ["Interstellar", "The Martian"],
        "The Martian": ["Interstellar", "Gravity", "Apollo 13"],
        "Hidden Figures": ["Contact", "Apollo 13"],
        "Apollo 13": ["The Martian", "Hidden Figures"],
    }

    print("\n=== GRAPH STRUCTURE ===")
    for movie, related_movies in graph.items():
        print(f"{movie}: {related_movies}")

    # ===============================
    # TODO (Student): BFS TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Select a starting node.
    # 2. Perform BFS traversal.
    # 3. Display the traversal order.
    # 4. Use comments to explain how BFS visits nodes level by level.
    # 5. Add at least one additional node or edge
    #    and demonstrate the updated traversal.

    print("\n=== BFS TRAVERSAL ===")
    start_movie = "Arrival"
    print(f"Starting at {start_movie}: {bfs(graph, start_movie)}")
    # Add a new movie and connect it to an existing movie. BFS now includes
    # this new recommendation when it reaches the connected movie.
    add_edge(graph, "Contact", "Ex Machina")
    print("After adding Ex Machina connected to Contact:")
    print(f"Updated traversal: {bfs(graph, start_movie)}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Start from a different node
    # - Use a disconnected graph
    # - Handle a missing start node safely
    # - Graph containing only one node
    # - Empty graph
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    # Starting elsewhere changes the order, because BFS is relative to start.
    print("Different starting node (Gravity):", bfs(graph, "Gravity"))

    # A disconnected component is not reachable from Arrival and is omitted.
    disconnected_graph = {"A": ["B"], "B": ["A"], "C": ["D"], "D": ["C"]}
    print("Disconnected graph from A:", bfs(disconnected_graph, "A"))

    # Missing start and empty graph return empty traversal lists safely.
    print("Missing start node:", bfs(graph, "Unknown Movie"))
    print("Empty graph:", bfs({}, "Arrival"))

    # A one-node graph visits only its starting node.
    print("Single-node graph:", bfs({"Solo": []}, "Solo"))

    # A cycle verifies that visited prevents endless revisiting.
    cycle_graph = {"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]}
    print("Cyclic graph:", bfs(cycle_graph, "A"))


if __name__ == "__main__":
    main()
