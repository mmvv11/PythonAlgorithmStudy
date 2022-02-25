size = 5
directionCode = "R R R U D D"

position = [1, 1]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
direction = ["U", "D", "L", "R"]


def move(code):
    x = position[0] + dx[direction.index(code)]
    y = position[1] + dy[direction.index(code)]

    if x < 1 or y < 1 or x > size or y > size:
        return

    position[0] = x
    position[1] = y
    return position


for command in directionCode.split():
    move(command)

print(position[0], position[1])
