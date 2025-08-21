import sys
input = sys.stdin.readline
'''
크기가 2^N x 2^N인 2차원 배열을 z모양으로 탐색
N > 1 인 경우, 2^N-1 x 2^N-1로 4등분 한 후에 재귀적으로 순서대로 방문
N이 주어질 대, r행 c열을 몇 번째로 방문하는지 출력
'''
# 기본 0에서 더해둬야될 수를 들고 재귀에 들어갈 거임
# 최종적으로 들고 들어간 숫자가 정답이 될 예정
# 또한, 각 재귀에서의 좌표들을 1사분면으로 옮겨준다.
def recur(cnt, r, c, num:int):
    global result
    if cnt == N:    # 최대 깊이로 들어가면 return
        result = num
        return
    
    # 현재 필드에서의 1사분면
    if r <= 2**(N-cnt-1) -1 and c <= 2**(N-cnt-1) -1:
        recur(cnt+1, r, c, num)
    
    elif r <= 2**(N-cnt-1) -1 and c > 2**(N-cnt-1) -1:    # 2사분면
        recur(cnt+1, r, c - 2**(N-cnt-1), num+2**(2*(N-1-cnt)))

    elif r > 2**(N-cnt-1) -1 and c <= 2**(N-cnt-1) -1:    # 3사분면
        recur(cnt+1, r - 2**(N-cnt-1), c, num+(2**(2*(N-1-cnt))*2))
    
    elif r > 2**(N-cnt-1) -1 and c > 2**(N-cnt-1) -1:     # 4사분면
        recur(cnt+1, r - 2**(N-cnt-1), c - 2**(N-cnt-1), num+(2**(2*(N-1-cnt))*3))

N, r, c = map(int, input().split())
result = 0
recur(0, r, c, 0)
print(result)