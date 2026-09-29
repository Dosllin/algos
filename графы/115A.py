# Ты менеджер среднего звена

n = int(input())
points = [0] + [int(input()) for _ in range(n)]

max_depth = 0
for i in range(1,n+1):
    curr = i
    depth = 0
    while curr!=-1:
        depth += 1
        curr = points[curr]
    if depth > max_depth:
        max_depth = depth
print(max_depth)
