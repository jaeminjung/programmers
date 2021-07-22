import math

def solution(w, h):
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    # print(gcd(w, h))
    g = gcd(w, h)

    total = w * h
    damage = 0
    angle = h / w
    for i in range(int(w / g)):
        damage += math.ceil(i * angle) - math.floor((i - 1) * angle)
    total -= damage * g

    return total

print(solution(8, 12))

#
# def solution(w, h):
#     def gcd(a, b):
#         if b == 0:
#             return a
#         return gcd(b, a % b)
#
#     # print(gcd(w, h))
#     g = gcd(w, h)
#     repeat = w / (g / w)
#
#     total = w * h
#     damage = 0
#     angle = h / w
#     before = 0
#     for i in range(g / w):
#         damage += math.ceil(i * angle) - math.floor((i - 1) * angle)
#
#     return total