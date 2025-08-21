def recur(cnt, num):
    global a
    if cnt == 5:
        a = num
        return
    print('____')
    recur(cnt+1, num +3)

a = 0
result = recur(0, 0)
print(a)