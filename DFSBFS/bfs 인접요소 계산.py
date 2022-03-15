from collections import deque

n = 4
m = 5

graph = [
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    """
    주변 노드 bfs를 돌려서 탐색이 모두 완료되면 true를 반환하자
    """
    if graph[x][y] == 1:
        return False

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 갈 수 없으면 재끼고
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                continue
            # 갈 수 있으면 값에
            if graph[nx][ny] == 0:
                graph[nx][ny] = 1
                queue.append((nx, ny))
    return True

result = 0
for i in range(n):
    for j in range(m):
        if bfs(i, j) == True :
            result += 1

print(result)