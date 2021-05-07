from itertools import chain


def solution(land, P, Q):
    line = list(chain.from_iterable(land))
    line.sort()
    n = len(line)

    cost = (sum(line) - line[0] * n) * Q
    answer = cost

    for i in range(1, n):
        if line[i] != line[i - 1]:
            cost = cost + ((line[i] - line[i - 1]) * i * P) - ((line[i] - line[i - 1]) * (n - i) * Q)
            if answer < cost:  
                break
            answer = min(answer, cost)
    return answer
