def SmallString(str):
    max=0
    arr = [str[i: j] for i in range(len(str))
           for j in range(i + 1, len(str) + 1)]
    for i in range(len(arr)):
        max_dis=len(set(arr[i]))
        charc=len(arr[i])
        if(max_dis==charc):
            if(max<max_dis):
                max=max_dis
    return max

string=input()
print(SmallString(string))