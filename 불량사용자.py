import re

def solution(user_id, banned_id):

    print(user_id)
    print(banned_id)
    answer = 0
    a = 1
    b_ = []
    for ban in banned_id:
        reg = ban.replace("*", "\w")
        reg += '$'
        print(reg)

        count = 0
        b = []
        for i, id in enumerate(user_id):
            if re.match(reg, id) is not None:
                print(reg, id)
                count += 1
                b.append(i)
        a *= count
        b_.append(b)

    print(a)
    print(b_)
    return answer



# solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"]) # 2
# solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["*rodo", "*rodo", "******"]) # 2
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"]) # 3

l1 = [1,2,3]
l2 = [1,3,2]

l1 = set(l1)
l2 = set(l2)
l = [l1, l2]
print(l1 in l)
print(l1, l2)
# print(l1 == l2)
# p1 = re.match('fr\wd\w', 'frodo')
# print(p1)
# p2= re.match('fr\wd\w', 'fradi')
# print(p2)
# p3= re.match('fr\wd\w', 'dradi')
# print(p3)
