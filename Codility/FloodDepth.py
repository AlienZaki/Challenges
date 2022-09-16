"""
https://app.codility.com/programmers/trainings/1/flood_depth/
"""


def solution(A):
    max_depth = 0
    for i in range(len(A)):
        maxL = max(A[:i])
        maxR = max(A[i + 1:])
        if i > 0 and A[i] <= maxL and i != (len(A) - 1) and A[i] < maxL and A[i] < maxR:
            depth = min(maxL, maxR) - A[i]
            #print(i, depth)
            max_depth = depth if depth > max_depth else max_depth
    return max_depth


A = [15, 13, 5, 7, 4, 10, 12, 8, 2, 11, 6, 9, 3]
print(solution(A))


