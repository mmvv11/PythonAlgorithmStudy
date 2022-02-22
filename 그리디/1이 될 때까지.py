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
