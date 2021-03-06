# 12914. 멀리 뛰기

**Level3**

https://programmers.co.kr/learn/courses/30/lessons/12914

# 풀이

간단한 DP 문제이다.

- 아무 칸도 뛰지 않는 경우(0칸) = 경우의 수 1개
- 1칸만 뛰는 경우 = 경우의 수 1개
- 2칸만 뛰는 경우 = 1칸만 뛰는 경우 + 2칸으로 뛰는 경우 = 2개
- 3칸만 뛰는 경우 = 1칸만 뛰는 경우 + 2칸만 뛰는 경우 = 3개

위 사실을 바탕으로 점화식을 세우면 아래와 같다

```
dp[n칸을 뛰기 위한 경우의 수] = dp[n-1칸을 뛰기 위한 경우의 수] + dp[n-2칸을 뛰기 위한 경우의 수]
```
