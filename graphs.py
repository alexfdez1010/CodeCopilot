def floyd(graph: list) -> list:
    """
    Calculate the shortest path between all the nodes of the graph represented by an adjacency matrix

    :param: graph: the graph represented in adjacency matrix
    :return: the distance between all the nodes
    """
    n = len(graph)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    return graph


def dijkstra(graph: list, node: int) -> list:
    """
    Calculate the shortest path from node in a graph represented by an adjacency list

    :param graph: the graph represented in adjacency list
    :param node: the node where to start
    :return: the distance between all the nodes and the node
    """
    n = len(graph)
    dist = [float('inf')] * n
    dist[node] = 0
    visited = [False] * n
    visited[node] = True
    for i in range(n):
        min_dist = float('inf')
        min_node = -1
        for j in range(n):
            if not visited[j] and dist[j] < min_dist:
                min_dist = dist[j]
                min_node = j
        visited[min_node] = True
        for j in range(n):
            dist[j] = min(dist[j], dist[min_node] + graph[min_node][j])
    return dist


def prim(graph: list) -> list:
    """
    Calculate the minimum spanning tree of graph using Prim's algorithm

    :param graph: the graph represented in an adjacency list
    :return: the minimum spanning tree
    """
    n = len(graph)
    dist = [float('inf')] * n
    dist[0] = 0
    visited = [False] * n
    visited[0] = True
    for i in range(n):
        min_dist = float('inf')
        min_node = -1
        for j in range(n):
            if not visited[j] and dist[j] < min_dist:
                min_dist = dist[j]
                min_node = j
        visited[min_node] = True
        for j in range(n):
            dist[j] = min(dist[j], dist[min_node] + graph[min_node][j])
    return dist


def kruskal(graph: list) -> list:
    """
    Calculate the minimum spanning tree of graph using Kruskal's algorithm

    :param graph: the graph represented in an adjacency list
    :return: the minimum spanning tree
    """
    n = len(graph)
    mst = []
    visited = [False] * n
    for i in range(n):
        for j in range(n):
            if graph[i][j] != float('inf'):
                mst.append((i, j, graph[i][j]))
    mst.sort(key=lambda x: x[2])
    mst_tree = []
    for edge in mst:
        if not visited[edge[0]] and not visited[edge[1]]:
            mst_tree.append(edge)
            visited[edge[0]] = True
            visited[edge[1]] = True
    return mst_tree


def bfs(graph: list, node: int) -> list:
    """
    Calculate the shortest path from node in a graph represented by an adjacency list

    :param graph: the graph represented in adjacency list
    :param node: the node where to start
    :return: the distance between all the nodes and the node
    """
    n = len(graph)
    dist = [float('inf')] * n
    dist[node] = 0
    visited = [False] * n
    visited[node] = True
    queue = [node]
    while len(queue) > 0:
        current = queue.pop(0)
        for i in range(n):
            if not visited[i] and graph[current][i] != float('inf'):
                dist[i] = min(dist[i], dist[current] + graph[current][i])
                queue.append(i)
                visited[i] = True
    return dist


def dfs(graph: list, node: int) -> list:
    """
    Calculate the shortest path from node in a graph represented by an adjacency list

    :param graph: the graph represented in adjacency list
    :param node: the node where to start
    :return: the distance between all the nodes and the node
    """
    n = len(graph)
    dist = [float('inf')] * n
    dist[node] = 0
    visited = [False] * n
    visited[node] = True
    stack = [node]
    while len(stack) > 0:
        current = stack.pop()
        for i in range(n):
            if not visited[i] and graph[current][i] != float('inf'):
                dist[i] = min(dist[i], dist[current] + graph[current][i])
                stack.append(i)
                visited[i] = True
    return dist


def edmond_karp(graph: list, source: int, sink: int) -> int:
    """
    Calculate the maximum flow in a graph represented by an adjacency list

    :param graph: the graph represented in adjacency list
    :param source: the source node
    :param sink: the sink node
    :return: the maximum flow
    """
    n = len(graph)
    flow = [0] * n
    flow[source] = float('inf')
    while True:
        path = bfs(graph, source)
        if path[sink] == float('inf'):
            break
        augment = float('inf')
        current = sink
        while current != source:
            augment = min(augment, graph[path[current]][current] - flow[path[current]])
            current = path[current]
        current = sink
        while current != source:
            flow[path[current]] += augment
            flow[current] -= augment
            current = path[current]
    return sum(flow)
