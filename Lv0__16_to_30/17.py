'''
정수 내림차순으로 배치하기

함수 solution은 정수 n을 매개변수로 입력받습니다.
n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요.
예를들어 n이 118372면 873211을 리턴하면 됩니다.

'''
#join()을 이용하여 합치고, sorted 합수로 정렬, reverse 속성으로 역순 배열
def solution(n):
    return int("".join(sorted(str(n), reverse=True)))
