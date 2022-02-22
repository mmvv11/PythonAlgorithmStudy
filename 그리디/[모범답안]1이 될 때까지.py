n = 25
k = 3
count = 0

result = 0

while True:
    # 나누어 떨어지는 수가 될 때까지 빼주기
    target = (n // k) * k  # 나누어 떨어지기 위해 되야하는 수
    result += (n - target)  # 몇번 빼야하냐
    n = target

    # 더이상 나눌 수 없을때 탈출
    if n < k:
        break

    # 나누기
    result += 1
    n = n // k

result += (n - 1)
print(result)
