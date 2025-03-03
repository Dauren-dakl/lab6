def counting(str):
    CNT= 0
    cnt = 0
    for i in str:
        if str[i].isupper():
           CNT+=1
        elif str[i].islower():
            cnt+=1
    return CNT , cnt

str = input()
print(counting(str))

