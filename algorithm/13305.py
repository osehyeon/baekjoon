num1 = int(input())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

max = num1 - 1 
sum = 0
while(len(list2) != 0): 
    len1 = list2.index(min(list2))
    for i in range(len1, max):
        sum += min(list2) * list1[i]
    max = len1
    list2 = list2[:len1]

print(sum)