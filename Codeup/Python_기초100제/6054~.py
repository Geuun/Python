# 6054
# https://codeup.kr/problem.php?id=6054

from distutils.spawn import spawn
from operator import xor
from posixpath import split


a , b = input().split()

print(bool(int(a) and int(b)))

## 위는 내가 적은 코드 아래는 정답.

a, b = input().split()

print(bool(int(a)) and bool(int(b)))

### 왜 틀렸다고 나오는거지...

# 6055
# https://codeup.kr/problem.php?id=6055

a, b = input().split()

print(bool(int(a) or int(b)))

# 6056
# https://codeup.kr/problem.php?id=6056

a, b = input().split()

A = bool(int(a))
B = bool(int(b))

print((A and (not B)) or ((not A)and B) )


# 6057
# https://codeup.kr/problem.php?id=6057

a, b = input().split()

A = bool(int(a))
B = bool(int(b))

print(  (A and B) or ((not A) and (not B)) )


# 6058
# https://codeup.kr/problem.php?id=6058

a, b = input().split()

A = bool(int(a))
B = bool(int(b))

print( ( not A ) and ( not B) )


# 6059
# https://codeup.kr/problem.php?id=6059

a = input()

print(~a)

print(int(A))

### 비트단위(bitwise) 연산자는,
### ~(bitwise not), &(bitwise and), |(bitwise or), ^(bitwise xor),
### <<(bitwise left shift), >>(bitwise right shift)