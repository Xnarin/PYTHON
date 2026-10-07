from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    box = [[-1 for _ in range(110)] for _ in range(110)] # -1은 없는 곳

    visit = [[False for _ in range(110)] for _ in range(110)] # 방문 여부

    dl = [(0,-1), (0, 1), (-1, 0), (1, 0)] # 좌우상하
    dq = deque()

    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, r) # 좌표를 2배로 늘려서 표현 map은 함수를 모든 값에 적용하시오
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                # 내부 공간이라면 0 외곽은 1
                if x1 < i < x2 and y1 < j < y2:
                    box[i][j] = 0
                elif box[i][j] != 0: # 내부가 아니라면 1로 외곽이라는 표시를 한다
                    box[i][j] = 1
    # for i in box:
    #    print(*i) # 압축을 풀어주는 것

    cx, cy = characterX*2, characterY*2
    ix, iy = itemX*2, itemY*2
    dq.append((cx, cy)) # 시작점 좌표와
    visit[cx][cy] = True

    # bfs
    while dq:
        x, y = dq.popleft()
        if x == ix and y == iy: # 아이템 좌표에 도착하면
            answer = visit[x][y] // 2 # 이동거리 2배로 늘렸으므로 2로 나눠준다
            break

        for k in range(4):
            nx, ny = x + dl[k][0], y + dl[k][1]
            if box[nx][ny] == 1 and not visit[nx][ny]: # 범위 안에 있고 외곽이고 방문하지 않았다면
                visit[nx][ny] = visit[x][y] + 1 # 이동거리 증가
                dq.append((nx, ny)) # 큐에 넣는다
    return answer