# 60060. 가사 검색

**Level 4**

https://programmers.co.kr/learn/courses/30/lessons/60060

# 풀이

처음에는 Trie 자료구조를 활용해 풀이했으나 효율성에서 통과하지 못했고, 이분탐색을 이용하여 풀이함.

효율적인 탐색을 위해 bisect 모듈 사용.

탐색을 위해 주어진 단어들을 길이별로 정렬한 딕셔너리 생성.

쿼리에 주어진 ? 를 a와 z로 바꿔준 후 그 사이에 있는 단어를 탐색하면 된다.