my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}


def shortest_path(graph, start, target=''):
    """
    Find the shortest path between nodes in a weighted graph using Dijkstra's algorithm.

    This function calculates the shortest path from a start node to either a specific target node
    or to all other nodes in the graph. It also prints the distances and paths.

    Parameters:
    graph (dict): A dictionary representing the graph. Each key is a node, and the value is a list
                  of tuples, where each tuple contains a neighboring node and the distance to it.
    start (str): The starting node for the path calculation.
    target (str, optional): The target node. If not provided, paths to all nodes will be calculated.

    Returns:
    tuple: A tuple containing two dictionaries:
           - distances: A dictionary with nodes as keys and their shortest distances from the 
                        start as values.
           - paths: A dictionary with nodes as keys and lists representing the shortest path 
                    from the start to each node as values.

    Prints:
    For each target node (or all nodes if no target is specified), prints:
    - The distance from the start node to the target node.
    - The path from the start node to the target node.
    """
    unvisited = list(graph)
    distances = {node: 0 if node == start else float('inf') for node in graph}
    paths = {node: [] for node in graph}
    paths[start].append(start)

    while unvisited:
        current = min(unvisited, key=distances.get)
        for node, distance in graph[current]:
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                else:
                    paths[node].extend(paths[current])
                paths[node].append(node)
        unvisited.remove(current)

    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        if node == start:
            continue
        print(
            f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')

    return distances, paths


shortest_path(my_graph, 'A', 'F')
