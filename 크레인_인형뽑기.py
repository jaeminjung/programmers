# board	moves	result
# [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	[1,5,3,5,1,2,1,4]	4
b = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
m = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    answer = 0
    idx_init = [0] * len(board[0])
    for i in range(0, len(board[0])):
        for j in range(0, len(board)):
            if board[j][i] != 0:
                idx_init[i] = j
                break
    print(idx_init)

    box = []
    for col in moves:
        pick = idx_init[col-1]
        if pick > len(board) - 1:
            break
        doll_num = board[pick][col-1]
        idx_init[col-1] += 1
        box.append(doll_num)

        if len(box) > 1:
            if box[-1] == box[-2]:
                answer += 2
                box.pop()
                box.pop()

    return answer

print(solution(b, m))