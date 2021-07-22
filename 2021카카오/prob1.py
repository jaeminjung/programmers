import re

def solution(string):

    answer = ""
    string = string.lower()
    string = re.sub('[_-.]', '', string)
    print(string)
    # while string.count(".."):
    #     string = string.replace("..", ".")

    return string

# print(solution("............"))
print(solution("...!@BaT#*..y.abcdefghijklm")) # bat.y.abcdefghi
# print("bat.y.abcdefghi")

# a = "."
# a = list(a)
# a.pop(0)
# a = ''.join(a)
# print(a, "adf")