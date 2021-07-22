'''
평균 구하기
문제 설명
정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.
'''
def solution(arr):
    answer = 0
    for i in arr:
        answer += i #배열의 합
    return answer/len(arr)

#다른사람 풀이
def solution_(arr):
    return sum(arr) / len(arr)