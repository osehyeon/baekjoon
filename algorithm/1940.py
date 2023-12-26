N = int(input())
M = int(input())
list1 = list(map(int, input().split()))
list2 = sorted(list1)

cnt = 0
i = 0
j = N-1
 
while i < j:
    if list2[i] + list2[j] < M:
        i += 1 
    elif list2[i] + list2[j] > M:
        j -= 1
    else:
        cnt += 1
        i += 1
        j -= 1


