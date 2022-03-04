"""
완전탐색 문제

시:분:초 문자열 형태로 검사해서 3이 있는지 탐색
"""

hour = 5
count = 0

for h in range(hour+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                count += 1

print(count)