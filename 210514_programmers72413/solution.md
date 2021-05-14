# 72413. 합승 택시 요금

**Level 3**

https://programmers.co.kr/learn/courses/30/lessons/72413

# 풀이

1. 가중치가 있는 그래프에서 최소 요금을 구하기 위해 다익스트라 알고리즘을 사용하였다.
2. A와 B가 헤어지는 지점을 K라고 하면 ``요금 = dijkstra(S, K) + dijkstra(K, A) + dijkstra(K, B)``이고 주어진 모든 지점을 하나씩 K에 대입하여 문제를 풀이하면 된다.