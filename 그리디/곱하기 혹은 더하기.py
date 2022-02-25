input = "02984"
arr = []

for num in input:
    num = int(num)
    arr.append(num)

result = arr[0]

for num in arr[1:]:
    mul = result * num
    plus = result + num
    result = mul if mul > plus else plus

print(result)