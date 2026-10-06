dict_name = {

}

def verification(name):
    if name in dict_name:
        return True
    else:
        return False

n = int(input())
for _ in range(n):
    name = input()
    if verification(name):
        count = dict_name[name]
        new_name = name+str(count)
        while verification(new_name):
            count+=1
            new_name = name+str(count)
        dict_name[name] = count+1
        dict_name[new_name] = 1
        print(new_name)
    else:
        dict_name[name] = 1
        print("OK")

