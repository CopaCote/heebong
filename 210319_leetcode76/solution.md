# 76. Minimum Window Substring
**hard**
Given two strings ```s``` and ```t```, return the minimum window in ```s``` which will contain all the characters in ```t```. If there is no such window in ```s``` that covers all characters in ```t```, return the empty string ```""```.

문자열 S와 T를 입력받아 O(n)에 T의 모든 문자가 포함된 S의 최소 윈도우를 찾아라.

**Note** that If there is such a window, it is guaranteed that there will always be only one unique minimum window in ```s```.

 

**Example 1:**

```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
```

**Example 2:**

```
Input: s = "a", t = "a"
Output: "a"
```


**Constraints:**

```
1 <= s.length, t.length <= 105
s and t consist of English letters.
```

# 풀이

먼저 최소 윈도우를 찾기 위해서는 브루트 포스로 검색하는 방법이 있으나 문제의 조건에 ```O(n)```을 만족하여야 한다는 조건이 있기 때문에 ```O(n^2)```을 가지는 브루트 포스는 사용할 수 없다.

O(n)을 만족하기 위해서 투 포인터를 사용해 풀어보았다. 문자열의 처음부터 우측으로 이동하는 슬라이딩 윈도우를 사용하였으며, 만족하는 적절한 위치를 찾았을 경우 해당 위치로부터 좌우의 포인터 크기를 좁혀 나가는 투 포인터로 풀이하였다.

```
need = collections.Counter(t)
missing = len(t)
```
```need```는 필요한 문자 각각의 개수, ```missing```은 필요한 문자의 전체 개수로 한다.
```
for right, char in enumerate(s, 1):
  missing -= need[char] > 0
  need[char] -= 1
```
오른쪽 포인터인 ```right```의 값을 계속 늘려나가며 슬라이딩 윈도우의 크기는 계속 커지는 형태가 된다. 만약 현재 문자가 필요한 문자 ```need[char]```에 포함되어 있다면 필요한 문자의 전체 개수인 ```missing```을 1 감소하고, 해당 문자의 필요한 개수 ```need[char]```도 1 감소한다.
```
if missing == 0:
  while left < right and need[s[left]] < 0:
    need[s[left]] += 1
    left += 1
```
```missing```이 0이 되면 필요한 문자가 0이 되는 것이고 왼쪽 포인터를 더 줄일수 있는지 확인한다. 즉, ```need[s[left]]```가 0보다 작으면 0을 가리키고 있는 위치까지 왼쪽 포인터를 이동한다.
```
if missing == 0:
  ...
  if not end or right - left <= end - start:
    start, end = left, right
  need[s[left]] += 1
  missing += 1
  left += 1
```
```missing```이 0이 될 때까지 오른쪽 포인터와 ```need[s[left]]```가 0이 될 때까지의 왼쪽 포인터가 정답이게 된다. 이 값은 더 작은 값을 찾을 때까지 유지하다가 가장 작은 값인 경우 슬라이싱 결과를 리턴한다.