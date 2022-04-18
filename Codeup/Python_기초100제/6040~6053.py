# 6040
# https://codeup.kr/problem.php?id=6040

from posixpath import split


a, b = input().split()
c = int(a) // int(b)
print(c)

# 6041
# https://codeup.kr/problem.php?id=6041

a, b = input().split()
c = int(a) % int(b)
print(c)

# 6042
# https://codeup.kr/problem.php?id=6042

a = float(input())
print(format(a, ".2f"))

# 6043
# https://codeup.kr/problem.php?id=6043

a, b = input().split()
c = float( a ) / float(b) 
print(format(c, ".3f"))

# 6044
# https://codeup.kr/problem.php?id=6044

a, b = input().split()
A = int(a)
B = int(b)
C = A / B

print(A + B)
print(A - B)
print(A * B) 
print(A // B) 
print(A % B) 
print(format( C , ".2f" )) 

# 6045
# https://codeup.kr/problem.php?id=6045

a, b, c = input().split()

S = int(a) + int(b) + int(c)
M = int(S) / 3

print(S, format(M, ".2f"))

# 6046
# https://codeup.kr/problem.php?id=6046

n = int(input())

print( n << 1)

# 6047
# https://codeup.kr/problem.php?id=6047

a, b = input().split()

A = int(a)
B = int(b)

print( A << B )


# 6048
# https://codeup.kr/problem.php?id=6048

a, b = input().split()

A = int(a)
B = int(b)

print( A < B ) 

# 비교연산자 ( < , > , >= , ==, != ) 는 계산 결과를 True(참) / False(거짓) 으로 계산해 출력한다.

# 6049
# https://codeup.kr/problem.php?id=6049

a, b = input().split()

A = int(a)
B = int(b)

print(A == B)

# 6050
# https://codeup.kr/problem.php?id=6050

a, b = input().split()

A = int(a)
B = int(b)

print( B >= A ) 

# 6051
# https://codeup.kr/problem.php?id=6051

a, b = input().split()

A = int(a)
B = int(b)

print( A != B ) 

# 6052
# https://codeup.kr/problem.php?id=6052

a = int(input())

print(bool(a))

# 6053
# https://codeup.kr/problem.php?id=6053

a = bool(int(input()))

print(not a)
# not 은 반대 연산을 출력해준다.
