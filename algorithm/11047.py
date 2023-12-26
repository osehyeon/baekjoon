
list1 = list(map(int, input().split()))
list2 = []

for i in range(list1[0]):
    list2.append(int(input()))

list2.sort(reverse=True)

count = 0
num = list1[1]

for i in range(list1[0]):
    count += num // list2[i]
    num %= list2[i]
print(count)