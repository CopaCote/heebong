def solution(k, room_number):
    answer = []
    
    room = {}
    
    for n in room_number:
        num = room.get(n, 0)
        if num:
            tmp = [n]
            while True:
                i = num
                num = room.get(num, 0)
                if not num:
                    answer.append(i)
                    room[i] = i + 1
                    for j in tmp:
                        room[j] = i + 1
                    break
                tmp.append(num)
                
        else:
            answer.append(n)
            room[n] = n + 1
            
    return answer