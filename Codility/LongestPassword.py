"""
https://app.codility.com/demo/results/trainingZPBKAW-922/#
"""


def solution(S):
    words = S.split()
    longest_size = -1
    for word in words:
        num_digits = 0
        num_chrs = 0
        for c in word:
            if c.isdigit():
                num_digits += 1
            elif c.isalpha():
                num_chrs += 1
            else:
                num_digits, num_chrs = 0, 0
                break
        if num_chrs % 2 == 0 and num_digits % 2 != 0:
            longest_size = len(word) if len(word) > longest_size else longest_size
    return longest_size


S = 'test 5 a0A pass007 ?xy1'
print(solution(S))