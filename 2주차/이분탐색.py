# 이분탐색
# 데이터가 정령돼 있는 배열에서 특정한 값을 찾아내는 것을 이분탐색이라고 합니다.
# 배열의 중간에 있는 임의의 값을 선액하여 찾고자 하는 값 X와 비교를 합니다.
# X가 중간 값보다 작으면 중간 값을 기준으로 좌측의 데이터들을 대상으로,
# X가 중간값보다 크면 배열의 우축을 대상으로 다시 탐색을 하면서 해당값을 탐색합니다.

# 이분탐색 예시
def solution1(trump):
    left = 0
    right = len(trump)-1
    while(left <= right):
        mid = (left+right)//2
        if trump[mid] == 8:
            return mid
        elif trump[mid] < 8:
            left = mid+1
        elif trump[mid] > 8:
            right = mid-1
    return mid

