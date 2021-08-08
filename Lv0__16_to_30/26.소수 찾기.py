'''
소수 찾기

1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)
'''

def solution(n):            # 효율성 53점...
    answer = []
    for i in range(2, n+1):
        k=0
        for j in range(2, i+1):
            if i%j==0:
                k+=1
        if k==1:
            answer.append(i)
    return len(answer)

# 다른사람 풀이
def solution2(n):
    answer = 0
    prime = [False] * (n + 1)   # 에라토스테네스의 체
    # 에라토스 테네스의 체 만들기
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if prime[i] == False:
            for j in range(i + i, n + 1, i):
                prime[j] = True

    answer = prime.count(False) - 2
    return answer

'''
1부터 n까지 소수 본인을 제외한 소수의 배수를 소거해주는 방법인데,
가장 빠른 이유는 제곱한 수가 n을 넘어가는 수까지의 소수만을 확인하면 되기 때문이다.
예를 들면 n이 120이라고 가정했을 때, 11의 제곱은 121이므로 11보다 작은 소수의 배수만 지우면 된다.
11보다 작은 소수는 2,3,5,7이므로 이를 제외한 소수들의 배수를 소거해주면 된다.

 
0을 무시하기 위해 [False]*n+1 크기의 배열을 선언하고,
제곱근 n의 값을 구한다.
prime[i]가 False면, 소수이고 True이면 소수가 아니라고 생각하고
소수일 때, 해당 소수를 제외한 배수를 True로 바꿔주는 작업을 한다.
이후 False의 수를 카운트하고 0과 1에 무시하기위해 -2를 해준다.

출처 : https://zooonique.tistory.com/58
'''