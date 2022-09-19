

n = 5
bad = 4


def isBadVersion(v):
    return True if v == bad else False

for i in range(1, n+1):
    print(i, isBadVersion(i))


A = [i for i in range(1, n+1)]
version = A[int(len(A)/2)]
while isBadVersion(version):
    A = A[:int(len(A)/2)]
    version = A[int(len(A)/2)]
print(version)