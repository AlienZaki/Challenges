"""
https://app.codility.com/programmers/trainings/1/flood_depth/
"""


def solution(A):
    depths = []
    for i in range(len(A)):
        if i > 0 and A[i] <= max(A[:i]) and i != (len(A) - 1) and A[i] < max(A[:i]) and A[i] < max(A[i + 1:]):
            depth = min(max(A[:i]), max(A[i + 1:])) - A[i]
            #print(i, depth)
            depths.append(depth)

    max_depth = max(depths) if depths else 0
    return max_depth


A = [1, 3, 2, 1, 2, 1, 5, 3, 3, 4, 2]
print(solution(A))


