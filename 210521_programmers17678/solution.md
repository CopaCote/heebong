# 17678. 셔틀버스

**Level 3**

https://programmers.co.kr/learn/courses/30/lessons/17678

# 풀이

timetable에 저장된 승객들의 도착시간을 deque에 넣는다.
두 개의 큐가 모두 빌 때까지 schedule이라는 스택에 승객이나 버스가 떠나는 순서대로 쌓는다.
그리고 맨 마지막 버스를 기준으로 좌석이 남았다면 마지막 버스의 시간을, 좌석이 없으면 마지막 승객보다 1분 빠른 시간을 리턴했다.