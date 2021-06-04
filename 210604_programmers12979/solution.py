def solution(n, stations, w):
    my_houses = []
    s = 1
    e = 0
    for station in stations:
        e = station-w-1
        if s > e:
            pass
        else:
            my_houses.append([s, e])

        s = station+w+1

    if s > n:
        pass
    else:
        my_houses.append([s, n])

    count = 0
    for e in my_houses:
        a = (e[1] - e[0] + 1) // ((2*w)+1)
        b = (e[1] - e[0] + 1) % ((2*w)+1)
        count += a
        if b == 0:
            pass
        else:
            count += 1

    return count
