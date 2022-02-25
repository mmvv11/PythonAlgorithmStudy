"""
복기

1. direction은 딕셔너리가 아니라 리스트로 해도 인덱스 추출이 가능 뭐 크게 상관 없긴함
2. 매트리스 최대값도 고려해야함: 23줄에 if x < 1 or y < 1 or x > size or y > size: 이렇게 되어야함
"""

size = 5
directionCode = "R R R U D D"

position = [1, 1]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
direction = {"U": 0, "D": 1, "L": 2, "R": 3}


def move(directionCode):
    x = position[0] + dx[direction[directionCode]]
    y = position[1] + dy[direction[directionCode]]

    if x < 1 or y < 1:
        return

    position[0] = x
    position[1] = y
    return position


for command in directionCode.split():
    move(command)

print(position[0], position[1])
