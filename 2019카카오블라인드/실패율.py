def solution(N, stages):
    answer = []
    fail = []
    count_stage = [0 for i in range(N)]
    total = len(stages)
    for stage in stages:
        if stage == N + 1:
            continue
        count_stage[stage-1] += 1
    # print(count_stage)
    for (i, num) in enumerate(count_stage):
        fail.append((i+1, num/total))
        total -= num
    
    fail.sort(key=lambda x:x[1], reverse=True)
    # print(fail)
    for f in fail:
        answer.append(f[0])
    return answer


print(solution(5,	[2, 1, 2, 6, 2, 4, 3, 3])) #	[3,4,2,1,5]
print(solution(4,	[4,4,4,4,4])) # [4,1,2,3]