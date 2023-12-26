list1 = list(map(int, input().split()))
list2 = list(input())

count = 0

for i in range(list1[0]):
    if list2[i] == 'P':
        min1 = i - list1[1] if i - list1[1] >= 0 else 0
        max1 = i + list1[1] if i + list1[1] <= list1[0] else list1[0]
        list3 = list2[min1 : max1+1] 
        print(list3)  
        
        for j in range(len(list3)):
            print(j)
            if list3[j] == 'H':
                count += 1
                list2[min1+j] = 0
                break
                


print(count)