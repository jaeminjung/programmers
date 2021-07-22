
def solution(records):
    answer = []
    d = {}
    for record in records:
        a = record.split()
        print(a)
        if a[0] == 'Enter' or a[0] == 'Change':
            d.update({a[1]:a[2]})

    for record in records:
        a = record.split()
        if a[0] == 'Enter':
            name = d.get(a[1])
            answer.append(name + '님이 들어왔습니다.')
        elif a[0] == 'Leave':
            name = d.get(a[1])
            answer.append(name + '님이 나갔습니다.')
    
    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]