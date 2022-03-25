import sys

inf = int(1e9)  # 무한으로 10억 설정

# 노드와 간선의 갯수
n, m = map(int, input().split())
# 시작 노드 번호
start = int(input())
# 그래프
graph = [[] for _ in range(n + 1)]
# 방문 확인 리스트
visited = [False] * (n + 1)
# 최단 거리 테이블 무한으로 초기화
distance = [inf] * (n + 1)

# 모든 간선 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용은 c
    graph[a].append((b, c))

# 방문하지 않은 노드 중에서 최단거리가 가장 짧은 노드 번호
def getSmallestNode():
    minValue = inf
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n+1):
        if distance[i] < minValue and not visited[i]:
            minValue = distance[i]
            index = i
    return index

# 다익스트라 함수
def dij(start):
    # 시작 노드 초기화
    distance[start] = 0
    visited[start] = True
    # 시작점에서 거리
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1개 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단거리가 가장 짧은 노드를 꺼내서 방문처리
        now = getSmallestNode()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드를 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dij(start)

# 모든 노드에 가기 위한 최단거리
for i in range(1, n+1):
    # 도달할 수 없는 경우
    if distance[i] == inf:
        print("inf")
    # 도달할 수 있는 경우
    else:
        print(distance[i])