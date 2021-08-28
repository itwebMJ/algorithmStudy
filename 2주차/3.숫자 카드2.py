'''
숫자 카드 2
https://www.acmicpc.net/problem/10816

숫자 카드는 정수 하나가 적혀져 있는 카드이다.
상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가
몇 개 가지고 있는지 구하는 프로그램을 작성하시오.

첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다.
둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다.
숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지
구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고,
10,000,000보다 작거나 같다.
'''
n = int(input())
trump = list(map(int, input().split()))
 #[6, 3, 2, 10, 10, 10, -10, -10, 7, 3]

trump.sort()
m = int(input())
list2 = list(map(int, input().split()))

def solution1(trump, n):
    left = 0
    right = len(trump)-1
    while(left <= right):
        mid = (left+right)//2
        if trump[mid] == n:
            return mid
        elif trump[mid] < n:
            left = mid+1
        elif trump[mid] > n:
            right = mid-1
    return mid


# print(" ".join(str(cnt)))


# 다른 사람 풀이1
# https://kongpowder.tistory.com/127
n = int(input())
arr1 = list(map(int, input().split()))
dict1 = dict() # 숫자카드와 개수를 딕셔너리에 담기
for i in arr1:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1

m = int(input())
arr2 = list(map(int, input().split()))
for i in arr2:
    if i in dict1:
        print(dict1[i], end=' ') # 존재하는 숫자 카드라면
    else: print(0, end=' ') # 존재하지 않는 숫자 카드라면

import sys


# 찾는 값의 가장 작은 인덱스를 반환함
def binary_search(array, target):
    start, end = 0, len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            while mid > 0:
                if array[mid - 1] == target:
                    mid -= 1
                else:
                    break
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None

# 다른 사람 풀이2
# https://velog.io/@dongchyeon/%EB%B0%B1%EC%A4%80-10816%EB%B2%88-%EC%88%AB%EC%9E%90%EC%B9%B4%EB%93%9C-2

n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
my_cards = list(map(int, sys.stdin.readline().split()))
cards.sort()

card_dict = {}

for card in my_cards:
    if card not in card_dict:
        idx = binary_search(cards, card)
        if idx is not None:
            count = 0
            for i in range(idx, len(cards)):
                if cards[i] == card:
                    count += 1
                else:
                    break
        else:
            count = 0
        card_dict[card] = count

print(' '.join(str(card_dict[x]) for x in my_cards))