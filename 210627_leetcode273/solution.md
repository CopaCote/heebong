# 273. Integer to English Words

https://leetcode.com/problems/integer-to-english-words/

Convert a non-negative integer num to its English words representation.



Example 1:

```
Input: num = 123
Output: "One Hundred Twenty Three"
```
Example 2:

```
Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
```
Example 3:

```
Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
```
Example 4:

```
Input: num = 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
```

Constraints:

- ```0 <= num <= 231 - 1```

# 풀이

1. 가능한 모든 단어를 3개의 리스트에 저장한다
2. 끝에서 세 자리마다 순회하여 읽고 res에 저장한다
3. 세 자리마다 끊어 읽으며 res에 추가한다