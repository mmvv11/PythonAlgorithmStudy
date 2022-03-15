"""
탐색 범위가 주어져있고,
빠르게 최적해를 찾아야하는 경우임
이진탐색 돌리면 삽가능
"""

n = 4  # 떡 갯수
m = 18  # 요청한 떡 길이
arr = [19, 15, 10, 17]  # 주어진 떡
arr.sort()

start = 0  # 시작점
end = max(arr)  # 끝점


def binarySearch(start, end, target):
    """
    :param start: 이진탐색 시작
    :param end: 이진탐색 끝
    :param target: 탐색 대상
    :return: 최대 높이
    """

    # 언제까지? start < end 를 만족하는 동안 계속
    if start >= end:
        return None

    mid = (start + end) // 2 # 중간지점, 초기 9
    # 잘린 떡의 길이를 구해야함
    slicedArr = list(map(lambda x: x-mid, arr))

    # 만약 slicedArr 의 최댓값이 target보다 크다면,
    # start를 mid로 바꾼다.
    if max(slicedArr) > target:
        start = mid
        return binarySearch(start, end, target)

    # 만약 slicedArr 의 최댓값이 target보다 작다면,
    # end를 mid로 바꾼다.
    if max(slicedArr) < target:
        end = mid
        return binarySearch(start, end, target)


    # 만약 slicedArr 의 최댓값이 target과 같다면 mid가 최적해
    if max(slicedArr) == target:
        return mid

print(binarySearch(start, end, m))