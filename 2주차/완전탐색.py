# 완전탐색
# 가능한 모든 경우의 수를 다 구해서 값을 찾는 것을 완전탐색이라고 합니다.
# 결과 값이 가장 확실하지만 그만큼 시간이 가장 오래걸리는 탐색방법입니다.

# 반복문
def solution1(trump):
    for i in range(len(trump)):
        if trump[i] == 8:
            return  i
        return -1
# 재귀함수
def solution2(trump, loc):
    if trump[i] == 8:
        return loc
    else:
        return solution2(trump, loc+1)