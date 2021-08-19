'''
시저 암호

어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다.
 예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다.
 "z"는 1만큼 밀면 "a"가 됩니다. 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을
 완성해 보세요.
'''


def solution(s, n):
    answer = ''
    up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    low = up.lower()
    s_list = []
    for i in s:
        s_list.append(i)
    for j in range(len(s_list)):
        if s_list[j] in up:
            idx = up.index(s_list[j])
            answer += up[int((idx + n) % 26)]
        elif s_list[j] in low:
            idx = low.index(s_list[j])
            answer += low[int((idx + n) % 26)]
        elif s_list[j] == ' ':
            answer += ' '

    return answer