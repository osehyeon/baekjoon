
list1 = list(map(int, input().split()))

num1 = int(input())

screen_start = 1 
screen_end = list1[0]

box_start = 1 
box_end = list1[1]

count = 0

for i in range(num1):
    num2 = int(input())
    while num2 < box_start: 
        count += 1 
        box_start -= 1
        box_end -= 1
    while num2 > box_end:
        count += 1 
        box_end += 1
        box_start += 1
    
print(count)