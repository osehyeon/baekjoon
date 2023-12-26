
num1= int(input())

i_min = 1000000

for i in range(1, num1+1):
    idx = i 
    sum = i
    while(i != 0):
        sum += idx%10
        idx = idx // 10
    if sum == num1 and i_min > i:
        i_min = i

if i_min == 1000000:
    print(0)
else: 
    print(i_min)