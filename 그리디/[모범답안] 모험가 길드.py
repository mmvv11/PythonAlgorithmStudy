total = 5
fearData = "2 3 1 2 2"

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모함가의 수
data = list(map(int,fearData.split()))


for i in data: # 공포도를 낮은 것 부터 하나씩 확인하며
    count += 1 # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재 공포도 이상이라면 그룹 결성
        result += 1 # 총 그룹 수 증가
        count = 0 # 현재 그룹에 포함된 모험가 초기화

print(result)
