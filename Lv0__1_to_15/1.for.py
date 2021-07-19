'''
두 정수 사이의 합

문제 설명
두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.
'''

def solution(a, b):
    answer = 0
    if a==b:
        answer = a
    else:
        if b<a:
            temp = b
            b = a
            a = temp
        for a in range(a, b+1):
            answer += a
    return answer

def abs(a, b):      # 다른 사람 풀이) 절대값을 이용하여 풀이
    return (abs(a - b) + 1) * (a + b) // 2
print(solution(3, 5))