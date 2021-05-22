from collections import deque


def solution(n, t, m, timetable):
    timetable = [int(time[: 2]) * 60 + int(time[3:]) for time in timetable]
    timetable.sort()
    timeq = deque(timetable)

    busq = deque([[9 * 60 + t * i, m] for i in range(n)])

    schedule = []
    while timeq or busq:
        if timeq:
            cur_person = timeq[0]
        else:
            schedule.extend(busq)
            break

        if busq:
            cur_bus = busq[0]
        else:
            schedule.extend(timeq)
            break

        if cur_person <= cur_bus[0]:
            schedule.append(timeq.popleft())
            cur_bus[1] -= 1
        else:
            schedule.append(busq.popleft())

        if cur_bus[1] == 0:
            schedule.append(busq.popleft())

    for i in range(len(schedule) - 1, -1, -1):
        if type(schedule[i]) is list:
            if schedule[i][1] > 0:
                return '{:02}:{:02}'.format(schedule[i][0] // 60, schedule[i][0] % 60)
            else:
                return '{:02}:{:02}'.format((schedule[i - 1] - 1) // 60, (schedule[i - 1] - 1) % 60)
