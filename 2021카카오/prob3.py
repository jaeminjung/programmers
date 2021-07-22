
def solution(info, querys):
    answer = []
    total = {}

    for person in info:
        e = person.split(" ")
        print(e)
        for item in e:
            if total.get(item) is None:
                total[item] = {}
            else:

    print(total)

    for query in querys:
        q = query.split(" and ")
        q1 = q.pop(-1)
        q += q1.split(" ")
        # print(q)
    return answer


a = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
b = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
#[1,1,1,1,2,4]

print(solution(a, b))