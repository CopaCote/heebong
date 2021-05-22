from collections import deque


def solution(n, edge):
    answer = 0
    graph = {}
    visited = [0]*n

    for e in edge:
        graph[e[0]] = graph.get(e[0], []) + [e[1]]
        graph[e[1]] = graph.get(e[1], []) + [e[0]]

    queue = deque()
    queue.append(1)

    visited[0] = 1

    while queue:
        nodes = len(queue)
        for i in range(nodes):
            current = queue.popleft()
            for c in graph[current]:
                if visited[c-1] == 0:
                    visited[c-1] = 1
                    queue.append(c)

    return nodes
