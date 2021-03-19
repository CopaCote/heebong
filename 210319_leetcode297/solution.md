# 297. Serialize and Deserialize Binary Tree
**Hard**
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

이진 트리를 배열로 직렬화 하고, 반대로 역직렬화하는 기능을 구현하라.

**Clarification:** The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 

**Example 1:**

![serdeser](serdeser.jpg)

```
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
```
**Example 2:**

```
Input: root = []
Output: []
```

**Example 3:**

```
Input: root = [1]
Output: [1]
```

**Example 4:**

```
Input: root = [1,2]
Output: [1,2]
```

**Constraints:**

- The number of nodes in the tree is in the range ```[0, 10^4]```.
- ```-1000 <= Node.val <= 1000```

# 풀이

## 직렬화

이 문제는 별도의 직렬화 알고리즘에 대한 제한이 없기 때문에 BFS를 통해 풀이했다.
```
     A
    /\
   B  C
     /\
    D  E
```
위와 같은 트리를 BFS를 통하여 직렬화 한 경우 다음과 같은 배열과 동일한 형태가 된다.
```
[ #, A, #, B, C, #, #, D, E]
```
다만 문제를 풀이하기 위해 ```NULL``` 대신```#```으로 표현하여 저장했다.
이 문제의 경우 리턴 값을 문자열로 받게 했는데, 파이썬은 ```None```을 문자로 바꿀 수 없기 때문이다.

BFS를 통해 직렬화를 다음과 같이 구현하였다.

```
def seriallize(self, root: TreeNode) -> str:
  ...
  while queue:
    node = queue.popleft()
    if node:
      queue.append(node.left)
      queue.append(node.right)

      result.append(str(node.val))
    else:
      result.append('#')
  return result
```

## 역직렬화

직렬화와 동일하게 큐를 사용하여 역직렬화를 진행하였다. 먼저 문자열 형태인 입력값을 처리하기 위해 다음과 같이 구현하였다.

```
def deserialize(self, data: str) -> TreeNode:
  nodes = data.split()

  root = TreeNode(int(nodes[1]))
  queue = collections.deque([root])
  ...
```

```split()```으로 공백 단위로 문자열을 끊어 ```nodes```라는 리스트 변수로 만들어 주었다. 그다음, 트리로 만들어줄 노드 변수 ```root```부터 만들고 큐 변수 역시 만들었다. 이후 큐를 순회하며 왼쪽 자식과 오른쪽 자식 각각 별도의 인덱스를 부여하여 ```nodes```를 탐색한다.

```
def deserialize(self, data: str) -> TreeNode:
  ...
  index = 2
  while queue:
    node = queue.popleft()
    if nodes[index] is not '#':
      node.left = TreeNode(int(nodes[index]))
      queue.append(node.left)
    index += 1

    if nodes[index] is not '#':
      node.right = TreeNode(int(nodes[index]))
      queue.append(node.right)
    index += 1
    ...
```

단 데이터가 ```# #```일 경우 아무것도 리턴하지 않도록 예외처리를 해야 한다.
