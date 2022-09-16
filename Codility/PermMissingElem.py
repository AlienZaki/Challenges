"""
https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/
"""


def solution(A):
    missing = [i for i in range(1, len(A)+1) if i not in A]
    return missing[0] if missing else None



A = [2, 3, 1, 4]
print(solution(A))