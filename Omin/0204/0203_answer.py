# # 문제 1: 행렬 나선형 순회

# 문제 설명:
# M x N 크기의 행렬(2차원 리스트)이 주어질 때, 행렬의 원소들을 **나선형(Spiral order)**으로 순회하며 하나의 리스트로 반환하는 함수를 작성하세요.
# 나선형 순회는 행렬의 바깥쪽 테두리부터 시작하여 시계 방향으로 안쪽으로 들어가는 방식입니다.

# 예시 입력:

# matrix = [
#     [ 1,  2,  3,  4],
#     [ 5,  6,  7,  8],
#     [ 9, 10, 11, 12]
# ]


# 예시 출력:

# [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]


def spiral_order(matrix):
    if not matrix:
        return []
    
    result = []
    left, right = 0, len(matrix[0]) - 1
    top, bottom = 0, len(matrix) - 1
    
    while left <= right and top <= bottom:
        # 왼쪽 → 오른쪽
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        
        # 위 → 아래
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        if top <= bottom:
            # 오른쪽 → 왼쪽
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        
        if left <= right:
            # 아래 → 위
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    
    return result

# 예제 실행
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print(spiral_order(matrix))







# 문제 2: 2차원 리스트 요소 빈도수 계산
# 문제 설명:
# 정수들이 저장된 2차원 리스트(행렬)가 주어집니다.
# 행렬의 모든 요소를 탐색하여, 각 정수가 몇 번 등장했는지 계산하는 함수를 작성하세요.
# 결과는 딕셔너리 형태로, 키는 정수, 값은 등장 횟수를 반환합니다.

# 예시 입력:

# matrix = [
#     [3, 5, 1],
#     [2, 5, 9],
#     [5, 0, 4]
# ]

# {3: 1, 5: 3, 1: 1, 2: 1, 9: 1, 0: 1, 4: 1}

def count_matrix_elements(matrix):
    frequency = {}
    
    # for row in matrix:
    #     for num in row:
    #         if num in frequency:
    #             frequency[num] += 1
    #         else:
    #             frequency[num] = 1
                
    # return frequency

    for i in len(matrix):
        for j in len(matrix[0]):
            if matrix[i][j] in frequency:
                frequency[matrix[i][j]] += 1
            else:
                frequency[matrix[i][j]] = 1

    return frequency



# 예제 실행
matrix = [
    [3, 5, 1],
    [2, 5, 9],
    [5, 0, 4]
]
print(count_matrix_elements(matrix))




# 문제 3: 

# 조금 더 난이도 있는 문제
# 문제 4: 미로 탈출 (최단 경로 찾기)
# 문제 설명:
# 𝑁
# ×
# 𝑀
# N×M 크기의 미로가 주어집니다. 이 미로는 2차원 리스트로 표현되며,

# 0: 이동 가능한 경로
# 1: 벽(이동 불가능)
# 을 나타냅니다. 시작 위치는 (0, 0)이고, 미로의 출구는 (N-1, M-1)입니다. 이 때, 출구까지 가기 위한 최단 경로의 길이를 반환하는 함수를 작성하세요. 경로가 존재하지 않는다면 -1을 반환합니다.
# 예시 입력:

# python

# maze = [
#     [0, 1, 0, 0, 0],
#     [0, 1, 0, 1, 0],
#     [0, 0, 0, 1, 0],
#     [1, 1, 0, 1, 0],
#     [0, 0, 0, 0, 0]
# ]
# 예시 출력:
# 9
# (위 미로에서 최단 경로의 길이는 9임)

# 도전 포인트:

# **BFS (너비 우선 탐색)**를 활용하여 최단 경로 문제를 해결해 보세요.
# 좌표 처리를 위해 tuple이나 collections.deque 등의 자료구조를 사용해 보세요.
# 미로의 크기가 임의로 커질 수 있으므로, 시간 복잡도를 고려한 효율적인 코드를 작성해 보세요.
# 경로를 찾는 것뿐만 아니라, 실제 경로(예: 좌표 리스트)를 반환하도록 확장해 볼 수도 있습니다.
# 힌트:

# 시작 지점 (0,0)부터 시작하여 각 단계마다 상하좌우로 이동 가능한 위치를 확인하세요.
# 이미 방문한 위치는 재방문하지 않도록 관리합니다.
# 각 위치에 도달하는 데 걸린 이동 횟수를 기록하면서, 목표 지점에 도달하면 이동 횟수를 반환하면 됩니다.

from collections import deque

def shortest_path_maze(maze):
    if not maze or maze[0][0] == 1:  # 시작점이 벽이면 이동 불가능
        return -1
    
    n, m = len(maze), len(maze[0])  # 행(N), 열(M)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우 이동 방향
    queue = deque([(0, 0, 1)])  # (행, 열, 이동 거리)
    visited = set((0, 0))  # 방문한 위치 기록
    
    while queue:
        x, y, dist = queue.popleft()
        
        if (x, y) == (n-1, m-1):  # 출구 도달 시 최단 거리 반환
            return dist
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, dist + 1))
    
    return -1  # 출구까지 도달할 수 없는 경우

# 예제 실행
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

print(shortest_path_maze(maze))


