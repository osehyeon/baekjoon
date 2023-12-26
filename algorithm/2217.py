from itertools import combinations

# 예시 데이터: 각 로프가 견딜 수 있는 중량

num1 = int(input())
ropes = [] 
for i in range(num1):
     ropes.append(int(input()))
# ropes = [10, 15, 20, 25]

# 최대 중량을 저장할 변수
max_weight = 0

# 가능한 모든 로프 조합에 대해 반복
for r in range(1, len(ropes) + 1):
    for combo in combinations(ropes, r):
        # 현재 조합에서 가장 약한 로프의 중량과 로프의 개수를 곱함
        current_weight = min(combo) * len(combo)
        # 최대 중량 갱신
        max_weight = max(max_weight, current_weight)

print(max_weight)
