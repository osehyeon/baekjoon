num1 = int(input())
list1 =list(map(int, input().split()))

list1.sort(reverse=True)

for i in range(1, num1):
    list1[i] = list1[i]/2
    
print(sum(list1))