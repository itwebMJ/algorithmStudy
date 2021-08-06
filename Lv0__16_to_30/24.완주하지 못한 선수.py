'''
완주하지 못한 선수

수많은 마라톤 선수들이 마라톤에 참여하였습니다.
단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한
선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을
return 하도록 solution 함수를 작성해주세요.
'''


def solution(participant, completion):
    completion.sort()
    participant.sort()
    for i in range(0, len(completion)):
        if completion[i] != participant[i]:
            return participant[i]
    return participant[i+1]  #동명이인 있을때

# 다른사람 풀이

import collections


def solution2(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]