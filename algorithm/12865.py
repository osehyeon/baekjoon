
list1 = list(map(int, input().split()))
list2 = [] 

for i in range(list1[0]):
    list2.append(list(map(int, input().split())))


def knapsack(N, K, items):
    # dp[i][w]는 처음 i개의 물건을 고려하고, 배낭의 무게 제한이 w일 때 담을 수 있는 최대 가치
    dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

    for i in range(1, N + 1):
        weight, value = items[i - 1]
        for w in range(1, K + 1):
            if weight <= w:
                # 현재 물건을 포함하는 경우와 포함하지 않는 경우 중 더 큰 가치를 선택
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
            else:
                # 현재 물건을 포함할 수 없는 경우
                dp[i][w] = dp[i - 1][w]

    return dp[N][K]


# 예제 출력 계산
max_value = knapsack(list1[0], list1[1], list2)
print(max_value)

