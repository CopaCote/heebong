# 49191.순위

https://programmers.co.kr/learn/courses/30/lessons/49191

# 풀이

DFS와 스택을 사용하여 풀이했다

1. n*n 배열 차트를 만들어 각 지점에 경기 결과를 기록한다
2. 한 사람씩 반복문을 돌며 이긴 경기에 대한 상대방을 wins에 저장한다
3. wins에서 진 사람들을 하나씩 pop하며 그들이 이긴 경기에 대해 진 사람들을 다시 wins에 넣어주고 이를 반복한다
4. chart 결과에서 1(win)이나 -1(lose)가 아닌 0으로 표현된것이 1개밖에 없으면(자기 자신과의 경기는 0) 순위를 알 수 있는 사람이므로 이들의 명수를 반환한다

