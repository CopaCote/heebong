# 64064. 불량 사용자

**Level 3**

https://programmers.co.kr/learn/courses/30/lessons/64064

# 풀이

1. 먼저 순열(permutation)을 사용해 list를 생성한다
2. user 목록과 ban 목록을 비교한 후 맞으면 answer에 추가한다
3. 단, 순서와 관계 없이 라는 조건이 붙었기 때문에 set 자료형으로 저장한다
4. answer의 길이를 반환한다

