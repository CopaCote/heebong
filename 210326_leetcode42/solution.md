# 42. Trapping Rain Water

**Hard**

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라.

**Example 1:**

![rainwatertrap](rainwatertrap.png)

```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
```

**Example 2:**

```
Input: height = [4,2,0,3,2,5]
Output: 9
```

**Constraints**:

- ```n == height.length```
- ```0 <= n <= 3 * 104```
- ```0 <= height[i] <= 105```

# 풀이

 이 문제를 풀기 위한 방법은 다양하지만, 여기서는 스택을 사용하였다. 스택을 쌓아 나가면서 현재 높이가 이전 높이보다 높을때, 즉 꺾이는 부분 변곡점을 기준으로 격차만큼 물 높이를 채웠다. 이전 높이는 계속 변화하기 때문에 스택에 채워 나가다가 변곡점을 만나면 스택에서 하나씩 꺼내 이전과의 차이만큼 물 높이를 채워나간다. 기본적으로 한 번씩 비교하기 때문에 O(n)에 풀이가 가능하다.

스택을 통한 변곡점 비교만 알아도 쉽게 풀 수 있는 문제이기 때문에 코드에 대한 별도의 설명은 추가하지 않았다.