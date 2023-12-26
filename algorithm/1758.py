def user_func(i, num):
    ans = num - (i - 1)
    if ans < 0:
        ans = 0
    return ans 

num1 = int(input())
list1 = []

for i in range(num1):
    list1.append(int(input()))

list1 = sorted(list1, reverse=True)

sum = 0
for i in range(0, num1):
    sum += user_func(i+1, list1[i])
    
print(sum)
