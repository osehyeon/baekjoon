num1 = int(input())
list1 = list(map(int, input().split()))

list1.sort()
sum = 0
max_sum = 0

if num1 % 2 == 0:
    for i in range(num1 // 2):
        sum = list1[i] + list1[-1-i]
        max_sum = max(sum, max_sum)
else:
    for i in range(num1 // 2):
        sum = list1[i] + list1[-2-i]
        max_sum = max(sum, max_sum)

print(max_sum)