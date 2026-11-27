# Unit 8 Discussion: Breadth-First Search (BFS)

## Overview

This assignment explored graph traversal using Breadth-First Search (BFS). I represented relationships with an adjacency list, traversed the graph with a queue, added a new connection, and tested edge cases.

## Learning Objectives

- Represented graphs using adjacency lists.
- Implemented BFS.
- Used a queue in graph traversal.
- Analyzed graph traversal behavior.

## Implementation

I implemented `bfs(graph, start)` using Python's `collections.deque`. The queue followed first-in, first-out (FIFO) order. I removed the next node from the front, added it to the traversal result, and enqueued its unvisited neighbors.

I stored visited nodes in a set and marked each node as visited when it was enqueued. This prevented cycles from causing repeated visits and ensured that each reachable node was processed once.

The graph represented movies connected by shared genres, casts, or audience preferences. I used an undirected adjacency list with seven initial movie nodes. I then added an additional movie and connection to demonstrate how the traversal changed.

## Edge Cases

I tested the following cases:

- **Different starting node:** BFS returned a traversal order relative to the new starting point.
- **Disconnected graph:** BFS visited only the component reachable from the selected start node.
- **Missing starting node:** The function returned an empty list instead of raising an error.
- **Empty graph:** The function returned an empty list.
- **Single-node graph:** BFS returned only the starting node.
- **Cyclic graph:** The visited set prevented nodes from being visited repeatedly.

## BFS and DFS Comparison

BFS explores a graph level by level. Its queue processes nodes in the order they are discovered, so BFS can find a shortest path in an unweighted graph. Its time complexity is O(V + E), where V is the number of vertices and E is the number of edges.

Depth-First Search (DFS) explores one branch as far as possible before backtracking. It is commonly implemented with recursion or a stack and also runs in O(V + E) when an adjacency-list representation is used.

BFS is preferable when finding the fewest-edge route or exploring nearby relationships first. DFS is useful when exploring deep paths, checking connectivity, or investigating all possible branches. BFS can use more memory on graphs with very wide levels, while DFS can use less memory on some graph shapes but may follow a long path before finding a desired result.

## Real-World Application

A streaming platform could represent movies as vertices and connect movies that share genres, actors, or audience preferences. Starting from a movie a user enjoyed, BFS could identify related titles one connection away before exploring titles connected through more distant relationships. This makes BFS useful when the platform wants to prioritize recommendations that are close to the user's known interests. DFS could instead explore a chain of related genres or titles deeply to discover less obvious recommendations.

## Discussion Board Reflection (150–200 words)

While completing this assignment, I learned how graphs represent relationships and how an adjacency list can store connections between items. I implemented Breadth-First Search using a queue and a visited set. The queue was important because it processed nodes in the order they were discovered, allowing the algorithm to explore the graph level by level. The visited set prevented repeated visits when the graph contained cycles.

One challenge was understanding how the starting node affected the traversal and how disconnected nodes should be handled. I addressed this by testing different starting points, a disconnected graph, a missing starting node, an empty graph, and a graph containing a cycle. I also added a new movie connection to demonstrate how the graph changed.

BFS and DFS both traverse graphs in O(V + E) time with adjacency lists, but they explore relationships differently. BFS is preferable when finding the shortest path in an unweighted graph or exploring nearby connections first. DFS is more appropriate when exploring deeper paths, backtracking, or investigating connected structures. For a streaming recommendation system, BFS could prioritize content closely related to a user's viewing history, while DFS could uncover more distant recommendations.

## Submission Checklist

- [x] Implemented BFS using a queue.
- [x] Used a visited set to prevent revisiting nodes.
- [x] Created an adjacency-list graph with at least six nodes.
- [x] Displayed the graph structure.
- [x] Demonstrated BFS traversal from a starting node.
- [x] Added a node and edge and demonstrated the updated traversal.
- [x] Tested different starts, disconnected graphs, missing starts, empty graphs, single-node graphs, and cycles.
- [x] Documented the implementation in past tense.
- [x] Included a 150–200-word reflection.
- [ ] Committed and pushed the Unit 8 files to GitHub.
- [ ] Added the repository link to the initial discussion post.
- [ ] Submitted the initial discussion post and two peer responses.

## Scope Note

The provided starter code and README specified BFS implementation. DFS is compared conceptually in the README and reflection because the supplied starter file did not include a DFS TODO or a DFS implementation requirement.
