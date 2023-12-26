num1 = int(input())

list1 = [] 

for i in range(num1):
    list1.append(int(input()))
    
list1.sort(reverse=True)
sum1 = 0
moc = num1//3

for i in range(moc+1):
    if(i != moc):
        sum1 += sum(list1[i*3:2+i*3])
    else:
        sum1 += sum(list1[i*3:])
    
print(sum1)    


