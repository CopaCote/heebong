# 42898.등굣길

**Level3**

https://programmers.co.kr/learn/courses/30/lessons/42898

# 풀이

DP를 사용한 간단한 문제이다. 가장 왼쪽 위에 있는 집은 (1, 1)로 나타내고 학교가 있는 좌표는 (m, n)으로 나타낸다.

격자의 크기 m, n과 물이 잠긴 지역의 좌표를 나타내는 2차원 배열 puddles가 매개변수로 주어진다.

집에서 학교까지 갈 수 있는 최단경로의 개수를 1,000,000,007로 나눈 나머지를 반환하면 된다.

먼저 IndexError를 방지하기 위해 왼쪽과 위쪽에 한줄씩 추가하고 초기값을 지정하였다.

```
dp = [[0] * (m+1) for _ in range(n+1)]
dp[1][1] = 1
```

이후 이중 for문을 통해 풀이를 진행하였다.

```
for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            if [j, i] in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
```

