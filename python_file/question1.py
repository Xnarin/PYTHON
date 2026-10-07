
def solution(cap, n, deliveries, pickups):
    answer = 0
    idx = n - 1 #인덱스 

    while(idx >= 0):
        # 배달과 수거가 모두 없는 경우
        if deliveries[idx] == 0 and pickups[idx] == 0:
            idx -= 1
            coutinue
        # 배달과 수거가 모두 있는 경우
        if(deliveries[idx] > 0 and pickups[idx] > 0):
            answer += (idx + 1) * 2
            # 배달과 수거를 동시에 처리
            deliveries[idx] -= cap
            pickups[idx] -= cap
            # 배달과 수거가 모두 처리된 경우
            if(deliveries[idx] <= 0 and pickups[idx] <= 0):
                idx -= 1
        # 배달만 있는 경우
        elif(deliveries[idx] > 0):
            answer += (idx + 1) * 2
            deliveries[idx] -= cap
            if(deliveries[idx] <= 0):
                idx -= 1

        # 수거만 있는 경우
        elif(pickups[idx] > 0):
            answer += (idx + 1) * 2
            pickups[idx] -= cap
            if(pickups[idx] <= 0):
                idx -= 1

    return answer