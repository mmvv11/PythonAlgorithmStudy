"""
복기

파이썬 내장 함수를 잘 활용했지만
지금 풀이로는 정렬이 필요가 없었음

cleanData 안에 num의 갯수를 세는 방법. count 메서드를 사용하지 않고 이렇게도 할 수 있음 ㅋㅋ 단, 정렬이 되어있어야함
"""

"""
for i in data: # 공포도를 낮은 것 부터 하나씩 확인하며
    count += 1 # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재 공포도 이상이라면 그룹 결성
        result += 1 # 총 그룹 수 증가
        count = 0 # 현재 그룹에 포함된 모험가 초기화
"""


total = 5
fearData = "2 3 1 2 2"

cleanData = sorted(fearData.split(" "))
cleanData = list(map(int, cleanData))
setData = set(cleanData)

result = 0

for num in setData:
    if cleanData.count(num) >= num:
        result += 1

print(result)