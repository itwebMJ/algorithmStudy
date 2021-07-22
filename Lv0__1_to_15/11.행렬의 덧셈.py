'''
행렬의 덧셈
문제 설명
행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을
서로 더한 결과가 됩니다. 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수,
 solution을 완성해주세요.
'''
def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        answer.append([])
        for j in range(len(arr1[i])):
            answer[i].append(arr1[i][j] + arr2[i][j])
    return answer

#다른 사람의 풀이

# zip() : 동일한 개수로 이루어진 자료형을 묶어주는 역할을 하는 함수
# A = [[1, 2], [2, 3]] B = [[3, 4], [5, 6]]
# print(zip(A, B)) # 출력 결과 : <zip object at 0x7fbcd592dc40>
# print(list(zip(A, B))) # 출력 결과 :[([1, 2], [3, 4]), ([2, 3], [5, 6])]

# for a, b in zip(A, B):
#   print(a, b)
# 출력 결과 : [1, 2] [3, 4] /n [2, 3] [5, 6]

