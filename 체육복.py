
def solution(n, lost, reserve):
    matched = 0
    l_point = 0
    r_point = 0
    while l_point < len(lost) and r_point < len(reserve):
        if lost[l_point] > reserve[r_point]:
            while lost[l_point] > reserve[r_point]:
                if lost[l_point] - 1 == reserve[r_point] or lost[l_point] + 1 == reserve[r_point]:
                    matched += 1
                    l_point += 1
                    break
                r_point += 1
                if l_point < len(lost) or r_point < len(reserve):
                    break

        elif lost[l_point] < reserve[r_point]:
            while lost[l_point] < reserve[r_point]:
                if lost[l_point] - 1 == reserve[r_point] or lost[l_point] + 1 == reserve[r_point]:
                    matched += 1
                    r_point += 1
                    break
                l_point += 1
                if l_point < len(lost) or r_point < len(reserve):
                    break

    return n - (len(lost) - matched)

# def solution(n, lost, reserve):
#
#     return 0

print(solution(5, [2, 4], [1, 3, 5]), 5) # 5
print(solution(5,[2, 4],[3]), 4) # 4
print(solution(3,[3],[1]), 2) # 2
