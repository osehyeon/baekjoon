# 돌 게임 승자 결정 프로그램

def determine_winner(n):
    # 돌의 개수가 4의 배수이면 창영이가 이길 수 있는 전략이 있음
    if n % 4 != 0:
        return "CY"
    else:
        # 그 외의 경우는 상근이가 이길 수 있는 전략이 있음
        return "SK"

winner = determine_winner(int(input()))
print(winner)


