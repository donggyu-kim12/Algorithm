import sys
from collections import deque
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    p = input().strip()          # 수행할 함수
    n = int(input().strip())     # 배열 크기
    temp = input().strip()

    if n == 0:
        arr = deque()
    else:
        arr = deque(map(int, temp[1:-1].split(',')))

    flag = False  # False → 정방향, True → 역방향
    error_flag = False

    for cmd in p:
        if cmd == 'R':
            flag = not flag
        else:  # D
            if not arr:
                print("error")
                error_flag = True
                break
            if not flag:
                arr.popleft()
            else:
                arr.pop()

    if not error_flag:
        if flag:
            arr.reverse()
        print("[" + ",".join(map(str, arr)) + "]")
