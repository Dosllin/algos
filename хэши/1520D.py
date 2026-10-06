t = int(input())
for _ in range(t):
    dict_repit ={}
    n = int(input())
    arr_points = [int(x) for x in input().split()]
    for idx,i in enumerate(arr_points, start=0):
        a = i-idx
        if a in dict_repit:
            dict_repit[a] += 1
        else:
            dict_repit[a] = 1
    total_pairs =0
    for count in dict_repit.values():
        total_pairs += count*(count-1)//2
    print(total_pairs)
