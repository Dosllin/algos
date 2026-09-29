# треугольник, деньги, самолёт

n = int(input())
points = [0] + [x for x in map(int,input().split())]

found = False

for i in range(1, n+1):
    a = points[i]
    b = points[a]
    c = points[b]
    if c == i:
        found = True
        break

if found:
    print("YES")
else:
    print("NO")
