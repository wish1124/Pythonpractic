from collections import deque


# 그래프 정의
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


# DFS (재귀 함수 사용)
def dfs(graph, node, visited):
    if node not in visited:
        visited.add(node)
        print(node, end=' ')
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)       
        

visited = set()
dfs(graph, 'A', visited)  # 출력: A B D E F C

print("\n")

# BFS
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    # A 가 queue 에 들어감.
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            print(node, end=' ')
            queue.extend(graph[node])
            print("queue: ", queue)



bfs(graph, 'A')  # 출력: A B C D E F




