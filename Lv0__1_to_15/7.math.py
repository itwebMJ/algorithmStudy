'''
가운데 글자 가져오기
문제 설명
단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요.
 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.
'''

def solution(s):
    answer = ''
    a = len(s)
    b = a//2        #  2로 나눈 몫
    if a % 2 != 0:
        answer = s[b]
    else:
        answer = s[b-1:b+1]     # 2글자 범위
    return answer


#다른 사람 풀이
def string_middle(str):
    return str[(len(str)-1)//2:len(str)//2+1]