import heapq

def find_medians(nums):
    min_heap = []  # 최소 힙 (큰 값들)
    max_heap = []  # 최대 힙 (작은 값들)
    medians = []

    for num in nums:
        # 첫 번째 숫자는 최대 힙에 삽입
        if not max_heap or num <= -max_heap[0]:
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)

        # 힙의 크기를 균형잡기
        if len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        if len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

        # 중간값 찾기
        medians.append(-max_heap[0])

    return medians

# 예제 입력
nums = []
N = int(input())

for i in range(N):
    nums.append(int(input()))
    print(find_medians(nums)[-1])
    
