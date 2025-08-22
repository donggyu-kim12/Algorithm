import sys
import heapq
input = sys.stdin.readline
'''
n개의 도시, m개의 버스
a에서 b로 가는데 드는 버스 비용의 최솟값과 경로를 출력해라.
- 출력 양식
비용
경로에 포함되어 있는 도시 개수(출발지, 도착지 포함)
방문하는 도시를 순서대로 출력
'''
def dijkstra(s):
    q = [(0, s)]
    distance[s] = 0
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for w, v in graph[now]:
            new = dist + w
            if new < distance[v]:
                distance[v] = new
                heapq.heappush(q, (new, v))
                way[v] = now



n = int(input())
m = int(input())
# 출발 도시의 번호, 도착 도시의 번호, 비용
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((w, b))
start, end = map(int, input().split())

distance = [float('inf')] * (n+1)
way = [0] * (n+1)   # 최소비용으로 목적지까지 갔을때의 경로를 구하는 배열

dijkstra(start)
print(distance[end])

result = [end]
for _ in range(n):
    result.append(way[end])
    end = way[end]
    if end == start:
        break
print(len(result))
for i in range(len(result)-1, -1, -1):
    print(result[i], end=' ')