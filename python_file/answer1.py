
def solution(cap, n, deliveries, pickups):
    # 총 이동 거리
    answer = 0
    idx = n - 1 #인덱스 
    # 배달 상자와 수거 상자의 개수
    deliver = 0;
    pickup = 0;

    # 가장 먼 집부터 시작
    for i in range(n-1, -1, -1):
        # 배달 / 수거 물량 누적
        deliver += deliveries[i]
        pickup += pickups[i]

        while(deliver > 0 or pickup > 0):
            deliver -= cap # 음수값으로 만들어서 
            pickup -= cap
            # 이동 거리 계산
            answer += (i + 1) * 2

    return answer