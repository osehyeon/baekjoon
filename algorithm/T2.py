def count_consecutive_sums_two_pointers(N):
    count = 0
    start = 1
    end = 1
    sum_of_numbers = 1  # 초기값은 첫 번째 숫자로 설정

    while end <= N:
        if sum_of_numbers < N:
            # 범위를 증가시키기 위해 end 포인터 이동
            end += 1
            sum_of_numbers += end
        elif sum_of_numbers > N:
            # 범위를 감소시키기 위해 start 포인터 이동
            sum_of_numbers -= start
            start += 1
        else:
            # 유효한 범위를 찾음
            count += 1
            # 다른 범위를 찾기 위해 end 포인터 이동
            end += 1
            sum_of_numbers += end

    return count

# 함수 사용 예시
result = count_consecutive_sums_two_pointers(15) # 여기서 15를 다른 N 값으로 변경 가능
print(result)
