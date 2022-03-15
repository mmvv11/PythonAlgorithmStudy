from collections import deque


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        # 현재 노드에 인접한 노드를 모두 검사 bfs 돌리기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 갈 수 없으면 재끼고
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            # 갈 수 있으면 값에 1을 더하고 큐에 넣으셈
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                
    # 도착점의 값을 리턴하셈
    return graph[n-1][m-1]


n = 5
m = 6

graph = [
    [1, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))
