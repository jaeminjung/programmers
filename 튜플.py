
def solution(s):
    a = []
    number = ""
    ex_set = set()
    isOpen = False
    s += ","
    for element in s:
        if element == "{":
            isOpen = True
        if element == "}":
            isOpen = False
        if element.isnumeric():
            number += element
        else:
            if element == ",":
                if isOpen:
                    ex_set.add(int(number))
                    number = ""
                else:
                    ex_set.add(int(number))
                    number = ""
                    a.append(ex_set)
                    ex_set = set()
    a.sort(key=len, reverse=True)
    # print(a)
    answer = []
    for i in range(len(a)-1):
        answer.append(list(a[i] - a[i+1])[0])
    answer.append(list(a[-1])[0])
    answer.reverse()
    return answer
print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))

# print({2,1,3} - {1,2})
# print({1,2} - {2,1,3})
# print(len({1,2}))
#
# a = {2,1,3} - {1,2}
# print(a[0])