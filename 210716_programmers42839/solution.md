# 42839. 소수 찾기

https://programmers.co.kr/learn/courses/30/lessons/42839

# 풀이

순열(permutations)을 사용해 완전탐색으로 풀이했다

```is_prime_number(n)``` 함수를 통해 소수인지 판별하였다

```permutation()``` 으로 주어진 모든 수의 순열을 생성한 뒤 반복문을 통해 소수인지 확인하고 소수일 경우 ```answer```에 추가했다

다만, 같은 값이 나올 수 있기 때문에 중복을 제거하기 위해 ```answer```은 ```set()```을 사용하였다