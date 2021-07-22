
def calculate(numbers, l1, l2, l3):
    result = 0
    op1 = l1.pop(0)
    count = 0
    for idx in l1:
        idx -= count
        numbers.insert(idx, eval(numbers.pop(idx) + op1 + numbers.pop(idx)))
        count += 1

    op2 = l2.pop(0)
    for idx in l2:
        idx -= count
        numbers.insert(idx, eval(numbers.pop(idx) + op2 + numbers.pop(idx)))
        count += 1
    return result

def solution(expression):
    answer = []
    numbers = []
    minus = ["-"]
    plus = ["+"]
    multi = ["*"]
    num = ""
    count = 0
    for i, s in enumerate(expression):
        if s.isnumeric():
            num +=  s
        else:
            numbers.append(num)
            num = ""
            if s == "-":
                minus.append(count)
            elif s == "+":
                plus.append(count)
            else:
                multi.append(count)
            count += 1
    numbers.append(num)
    print(numbers)
    print(plus)
    print(minus)
    print(multi)

    answer.append(calculate(numbers, plus, minus, multi))
    # answer.append(calculate(numbers, plus, multi, minus))
    # answer.append(calculate(numbers, multi, plus, minus))
    # answer.append(calculate(numbers, multi, minus, plus))
    # answer.append(calculate(numbers, minus, multi, plus))
    # answer.append(calculate(numbers, minus, plus, multi))

    return max(answer)


print(solution("100-200*300-500+20")) #	60420
# calculate(['100', '200', '300', '500', '20'], [3], [0, 2], [1])
# print(solution("50*6-3*2")) #	300
