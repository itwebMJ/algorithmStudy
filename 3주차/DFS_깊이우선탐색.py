# DFS 깊이 우선 탐색
# DFS는 깊이 우선 탐색이라고 하며, 미로를 탐색할 때 한 방향으로 갈 수 있을 때까지
# 계속 가다가 더 이상 갈 수 없게 되면 다시 가장 가까운 갈림길로 돌아와
# 다른방향으로 다시 탐색을 진행하는 방법과 유사하다고 보면 됩니다.
#
# 모든 노드를 방문 하고자 할 경우 많이 사용합니다.
# stack과 사용


# 미로찾기
# 탈출가능하면 True, 탈출 불가능한 미로라면 False
def solution(stack, dest, maps):
    hori, verti = 0, 0
    while len(stack) >0:
        now = stack.pop()
        if now == dest:
            return True
        x = now[1]
        y = now[0]
        if x - 1 > -1:
            if maps[y][x-1] == 0 :
                stack.append([y, x-1])
                maps[y][x-1]=2
        if x + 1 > hori:
            if maps[y-1][x+1] == 1 :
                stack.append([y, x+1])
                maps[y][x+1]=2
        if y - 1 > -1:
            if maps[y-1][x] == 1 :
                stack.append([y-1, x])
                maps[y-1][x]=2
        if y + 1 > verti:
            if maps[y+1][x] == 1 :
                stack.append([y+1, x])
                maps[y+1][x]=2
    return False