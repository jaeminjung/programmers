
def solution(participant, completion):
    p = {}
    for one in completion:
        if one in p:
            p[one] += 1
        else:
            p[one] = 0

    for name in participant:
        if name in p:
            if p[name] == 0:
                del p[name]
            else:
                p[name] -= 1
        else:
            return name

    # answer = ''
    # return answer

p = ["leo", "kiki", "eden"]
c = ["eden", "kiki"]
print(solution(p, c))
