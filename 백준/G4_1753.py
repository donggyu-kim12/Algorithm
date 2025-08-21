import sys
import heapq
input = sys.stdin.readline
'''
시작점에서 다른 모든 정점으로의 최단 경로를 구해라
경로 존재하지 않으면 INF출력
단방향 그래프
'''
def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for w, v in graph[now]:
            cost = dist + w
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(q, (cost, v))

            
# 정점은 1부터 V까지
# 정점, 간선 개수
V, E = map(int, input().split())
K = int(input())    # 시작 정점
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

distance = [float('inf')] * (V+1)
dijkstra(K)

for i in range(1, V+1):
    if i == K:
        print(0)
    else:  
        print('INF' if distance[i] == float('inf') else distance[i])
    