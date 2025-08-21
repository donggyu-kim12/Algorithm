'''
배추흰지렁이는 배추근처에서 해충 잡아먹으면서 배추를 보호.
한 마리라도 살고 있으면 지렁이는 인접한 배추로 이동 가능, 그 배추들도 보호받을 수 있음
한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우 서로 인접해있는 것
지렁이가 몇 마리 있어야 배추를 모두 보호가능한지?
'''
from collections import deque
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def bfs():
    result = 0
    q = deque()
    visited = [[0] * M for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0 or visited[i][j]:  # 배추가 없으면 pass
                continue
            
            q.append([i, j])
            visited[i][j] = 1   # 배추있으면 방문 check
            result += 1
            
            while q:
                r, c = q.popleft()
                for k in range(4):
                    nr, nc = r + dr[k], c + dc[k]
                    if nr < 0 or nc < 0 or nr >= N or nc >= M or arr[nr][nc] == 0:
                        continue
                    
                    if visited[nr][nc]:
                        continue
                    
                    q.append([nr, nc])
                    visited[nr][nc] = 1
                             
    return result      


# 테스트 케이스 개수
T = int(input())
for _ in range(T):
    # M : 배추밭 가로, N : 배추밭 세로, K : 배추 심어져 있는 위치의 개수
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    for _ in range(K):
        a, b = map(int, input().split())
        # 배추가 심어져 있는 곳은 1로 표시
        arr[b][a] = 1
   
    answer = bfs()
    print(answer)
