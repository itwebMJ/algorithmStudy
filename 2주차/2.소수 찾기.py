'''
https://programmers.co.kr/learn/courses/30/lessons/42839
소수 찾기
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때,
 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

'''

# 다른사람 풀이  - 출처 :  https://eda-ai-lab.tistory.com/466
from itertools import permutations
import math

# 순열 permutations 을 이용한 풀이

def check(n):
    k = math.sqrt(n)    # 제곱근을 아용하여 소수를 찾는 속도를 빠르게 함
    if n < 2:
        return False

    for i in range(2, int(k)+1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    answer = []
    for k in range(1, len(numbers)+1):
        perlist = list(map(''.join, permutations(list(numbers), k)))
        for i in list(set(perlist)):    # 자료형 set 으로 중복 제거
            if check(int(i)):
                answer.append(int(i))

    answer = len(set(answer))

    return answer

