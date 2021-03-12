# 179. Largest Number
**Medium**
Given a list of non-negative integers ```nums```, arrange them such that they form the largest number.
항목들을 조합하여 만들 수 있는 가장 큰 수를 출력하라.

**Note**: The result may be very large, so you need to return a string instead of an integer.

Example 1:
```
Input: nums = [10,2]
Output: "210"
```
Example 2:
```
Input: nums = [3,30,34,5,9]
Output: "9534330"
```
Example 3:
```
Input: nums = [1]
Output: "1"
```
Example 4:
```
Input: nums = [10]
Output: "10"
```
 

Constraints:

- ```1 <= nums.length <= 100```
- ```0 <= nums[i] <= 109```


# 풀이
삽입 정렬을 통해 풀 수 있는 문제이다. 주의해야 할 점은 주어진 숫자의 맨 앞자리수를 비교하여 크기 순으로 정렬해야 한다. 쉽게 비교하기 위하여 a + b와 b + a를 비교하는 형식으로 처리할 수 있다.
```
def to_swap(n1: int, n2: int) -> bool:
    return str(n1) + str(n2) < str(n2) + str(n1)
```
위 함수의 결과가 True이면 위치 변경이 이루어져야 한다. 삽입 정렬을 통해 위치를 바꿀 수 있다.

삽입 정렬의 수도코드는 다음과 같다.
```
i ← 1
while i < length(A)
    j ← i
    while j > 0 and A[j-1] > A[j]
        swap A[j] and A[j-1]
        j ← j - 1
    end while
    i ← i + 1
end while
```
단 ```A[j-1] > A[j]```에 해당되는 비교는 위에서 구현한 ```to_swap```을 활용해 비교하여야 한다.

삽입 정렬을 배열을 통해 구현하게 되면, 제자리 정렬이 가능하여 공간 복잡도를 줄일 수 있다.

마지막에 리턴하는 부분은 입력값이 ```["0", "0"]```인 경우 00이 아닌 0이 출력돼야 하므로 ```join()```의 결과를 int로 바꿔준 후 다시 str로 변경한다.