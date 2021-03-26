# 316. Remove Duplicate Letters

**Medium**

Given a string ```s```, remove duplicate letters so that every letter appears once and only once. You must make sure your result is **the smallest in lexicographical order** among all possible results.

중복된 문자를 제외하고 사전식 순서로 나열하라.

**Example 1:**

```
Input: s = "bcabc"
Output: "abc"
```

**Example 2:**

```
Input: s = "cbacdcbc"
Output: "acdb"
```

**Constraints:**

- ```1 <= s.length <= 104```
- ```s consists of lowercase English letters.```

# 풀이

난이도는 Medium이지만 사전식 순서로 정렬하라는 조건이 붙어 체감 난이도는 높았던 문제이다. 먼저 두 가지 방식으로 풀이를 할 수 있었는데, 재귀를 이용한 분리 방식과 스택을 이용한 분리 방식이 있었다. 재귀를 이용한 방식 역시 통과는 됐지만 실행 시간이 길다는 단점이 있었다.

만약 현재 문자 char가 스택에 쌓여 있는 문자이고, 뒤에 다시 붙일 문자가 남아 있다면, 쌓아둔 걸 꺼내서 없앤다. 예제의 입력값 cbacdbc에서 a가 들어올 때, 이미 이전에 들어와 있던 c와 b는 다음과 같이 제거된다.
```stack = XXXacdXbX```