# BFS 너비 우선 탐색
# BFS는 너비 우선 탐색이라고 하며, 말 그대로 시작 정점으로부터 가까운 정점을 먼저 방문하고,
# 멀리 떨어져 있는 정점을 나중에 방문하는 순회방법입니다.
#
# 두 노드 사이의 최단 경로 혹은 임의의 경로를 찾고 싶을 때 많이 사용합니다.
# queue과 사용


# 미로찾기
# 탈출가능하면 True, 탈출 불가능한 미로라면 False
def solution(queue, dest, data):
    answer = 0
    visited = []
    while len(queue) >0:
        count = len(queue)
        for time in range(count):
            now = queue.pop(0)
            if now == dest:
                return answer
            for i in data:
                if i[0]==now and visited[i[1]-1]==False:
                    queue.append(i[1])
                    visited[i[1] - 1] =True
                elif i[1]==now and visited[i[0]-1]==False:
                    queue.append(i[0])
                    visited[i[0] - 1] =True
        answer +=1

    return answer