num = int(input())

cnt = 0


while num: 
    if num == 1: 
        cnt = -1
        num = 0
    elif num % 5 != 0:
        num -= 2
        cnt += 1 
    elif num % 5 == 0:
        cnt += num // 5 
        num -= num
    

print(cnt)
        