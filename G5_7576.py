import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

q = deque()

# 처음부터 익은 토마토들을 모두 큐에 넣음
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append((i, j))

# BFS
while q:
    r, c = q.popleft()
    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
            arr[nr][nc] = arr[r][c] + 1   # 하루 뒤에 익음
            q.append((nr, nc))

# 결과 확인
result = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:   # 안 익은 토마토가 있으면
            print(-1)
            exit(0)
        result = max(result, arr[i][j])

print(result - 1)   # 처음 익은 토마토가 1이므로 -1
