
def solution(answers):
    aAnswer = [1, 2, 3, 4, 5]
    bAnswer = [2, 1, 2, 3, 2, 4, 2, 5]
    cAnswer = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    a, b, c = 0, 0, 0
    for i in range(len(answers)):
        f = answers[i]
        a1 = i % 5
        b1 = i % 8
        c1 = i % 10
        if f == aAnswer[a1]:
            a += 1
        if f == bAnswer[b1]:
            b += 1
        if f == cAnswer[c1]:
            c += 1
    answer = []
    answers = [a,b,c]
    max_num = max(answers)
    for i in range(3):
        if answers[i] == max_num:
            answer.append(i+1)
    return answer