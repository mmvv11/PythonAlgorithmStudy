"""
복기
k가 엄청 큰 수라면 최대 k-1 번만큼 반복문을 돌아야하는 비효율이 발생함
모범 답안 맹키로
    target = (n // k) * k  # 나누어 떨어지기 위해 되야하는 수
    result += (n - target)  # 몇번 빼야하냐
    n = target
몇번 빼야하는지 한번에 계산할 수 있음
"""

n = 25
k = 3
count = 0

while n > 1:
    # 나머지가 0인 경우
    if n % k == 0:
        n = n / k
        print(f"나누어 떨어지는 경우: n = {n}, count: {count}")
    # 나머지가 0이 아닌 경우
    else:
        n -= 1
        print(f"1을 빼야하는 경우: n = {n}, count: {count}")
    count += 1

print(f"n: {n}, count: {count}")
