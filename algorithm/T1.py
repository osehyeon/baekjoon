
# N 이 있으면 X(X+1)/2 - Y(Y+1)/2 = N 인 (X,Y)의 모음을 구하시오 (X>Y)

def user_func(num1, num2):
    return num1*(num1+1)/2 - num2*(num2+1)/2

num = int(input())

x = num 
y = 0
cnt = 0

while x != y: 
    if user_func(x, y) > num:
        y += 1
    elif user_func(x, y) == num:
        cnt += 1
        x -= 1 
        y = 0
    else:
        x -= 1 
        y = 0

print(cnt)



