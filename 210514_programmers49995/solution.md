# 49995. 쿠키 구입

**Level 4**

https://programmers.co.kr/learn/courses/30/lessons/49995

# 풀이

1. 주어진 배열의 크기를 n이라고 할 때 배열의 0번째부터 n-2번째 까지를 기준으로 하여 문제를 풀이한다.
2. 기준점을 포함하여 왼쪽은 첫째 아들에게 주는 과자, 기준점+1 부터 오른쪽은 둘째 아들에게 주는 과자이다.
3. 두 아들의 과자의 수를 비교하며 좌, 우로 넓혀가고 두 아들의 과자의 수가 같을 경우를 max로 저장하여 계속 업데이트 한다.
4. 기준점의 위치를 증가시키며 위 과정을 반복한다.