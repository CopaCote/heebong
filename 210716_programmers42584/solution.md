# 42584. 주식가격

https://programmers.co.kr/learn/courses/30/lessons/42584

# 풀이

스택으로 분류된 문제여서 스택을 사용한 풀이 위주로 접근했으나 이중 for문을 사용해 풀이하는것이 더 빠르다고 생각하여 풀이 방식을 바꿨다

i는 비교할 기준의 index가 된다
```if prices[i] > prices[j]```를 통해 가격이 떨어지는 시점까지 반복하다 떨어지게 되면 탈출하는 구조로 문제를 풀이하였다