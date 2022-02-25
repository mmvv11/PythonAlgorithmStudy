input = "02984"

result = int(input[0])

for num in input[1:]:
    num = int(num)
    # 두 수 중에서 하나라도 0, 1 인경우엔 곱하기보다 더하기 수행
    if num <=1 or result <=1:
        result += num
    else:
        result *= num


print(result)