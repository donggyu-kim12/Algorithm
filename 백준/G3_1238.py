import sys
import heapq
input = sys.stdin.readline
'''
N개의 숫자로 구분된 마을에 각각 한 명씩 살고 있음
단방향 도로, i번째 길을 지나는 데 T시간을 소비
각 학생들을 파티에 참석하기 위해 갔다가 돌아와야됨.
N명의 학생 중 오고 가는 데 가장 많은 시간을 소비한 사람의 소요 시간은?
'''
def dijkstra(s, arr:list):
    distance = [float('inf')] * (N+1)
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for w, v in arr[now]:
            if w + dist < distance[v]:
                distance[v] = w + dist
                heapq.heappush(q, (w+dist, v))
    return distance


# N개의 마을, X : 파티 장소
N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
re_graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, w = map(int, input().split())
    graph[a].append((w, b))
    re_graph[b].append((w, a))

v_to_X = dijkstra(X, re_graph)
X_to_v = dijkstra(X, graph)

result = 0
for i in range(1, N+1):
    result = max(v_to_X[i]+X_to_v[i], result)
print(result)
