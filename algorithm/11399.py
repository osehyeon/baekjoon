num1 = int(input())
list1 = list(map(int, input().split()))

list1.sort()

pre_people = 0 
now_peple = 0
list_people = [] 
for i in range(len(list1)):
    now_people = list1[i] + pre_people 
    list_people.append(now_people)
    pre_people = now_people


print(sum(list_people))