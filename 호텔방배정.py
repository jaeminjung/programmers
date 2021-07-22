
def check_next(d, num):
    next_num = num + 1

    while True:
        if d.get(next_num) is None:
            d[next_num] = next_num
            return next_num
        else:
            # if d.get(next_num) is not None:
            next_num = d[next_num]
            next_num += 1


def solution(k, room_number):
    answer = []
    d = {}
    d_ = {}
    for num in room_number:
        if d.get(num) is None:
            answer.append(num)
            d[num] = num
        else:
            avail = check_next(d, d[num])
            d[num] = avail
            answer.append(avail)
            # d[num] = avail

    return answer

#
d = {}

# d[1] = 2
# print(d[1])
# print(d.get(1) is None)

# print(solution(10, [1,3,4,1,3,1])) # [1,3,4,2,5,6]
print(solution(10, [1,1,1,2,1,1]))