import heapq

def solution(n, k, enemy):
    heap  = []
    sum_heap = 0;
    all_heap = 0;

    for i in range(n):
        heapq.heappush(heap, enemy[i])
        sum_heap += enemy[i]
        all_heap += enemy[i]
        
        if(len(heap) > k):
            sum_heap -= heapq.heappop(heap)
        cost = all_heap - sum_heap
        if(cost > n):
            return i

    return len(enemy)