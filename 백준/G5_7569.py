import sys
from collections import deque
input = sys.stdin.readline
'''
토마토는 보관 하루가 지나면 익은 토마토들의 인접해 있는 익지 않은
토마토는 익은 토마토의 영향을 받아 익음.(위,아래,앞뒤좌우)
며칠이 지나야 창고의 토마토가 다 익을지?
'''
# 가로, 세로, 상자의 수(높이)
M, N, H = map(int,input().split())
# 1 : 익은 것, 0 : 안 익은 것, -1 : 토마토 없는 칸
arr = []
for _ in range(H):
    temp = []
    for _ in range(N):
        row = list(map(int, input().split()))
        temp.append(row)
    arr.append(temp)

q = deque()

for i in range(H):          # 층
    for j in range(N):      # 행
        for k in range(M):  # 열
            if arr[i][j][k] == 1:
                q.append((i, j, k))

# 상하뒤앞좌우
dh = [-1, 1, 0, 0, 0, 0]    # 높이
dr = [0, 0, -1, 1, 0, 0]    # 행
dc = [0 ,0 ,0, 0, -1, 1]    # 열

while q:
    h, r, c = q.popleft()
    for k in range(6):
        nh, nr, nc = h + dh[k], r + dr[k], c + dc[k]
        if 0<=nh<H and 0<=nr<N and 0<=nc<M and arr[nh][nr][nc] == 0:
            q.append((nh, nr, nc))
            arr[nh][nr][nc] = arr[h][r][c] + 1

result = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 0:
                print(-1)
                exit()
            result = max(result, arr[i][j][k])
print(result - 1)
