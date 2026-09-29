
n, m = map(int, input().split())
cats = [int(x) for x in input().split()]
dir_points = {}
for _ in range(n-1):
    a, b = map(int, input().split())
    dir_points.setdefault(a, []).append(b)
    dir_points.setdefault(b, []).append(a)
visited = set()
ans = 0

def dfs(graph, start, visited, cats_count):
    global ans
    visited.add(start)
    if cats[start-1] == 1:
        cats_count += 1
    else:
        cats_count = 0
    if cats_count > m:
        return
    next_steps = set(dir_points[start])-visited
    if not next_steps:
        ans += 1
    else:
        for next in next_steps:
            dfs(graph, next, visited, cats_count)
dfs(dir_points, 1, visited, 0)
print(ans)
