# https://wikidocs.net/7022

# 21

letters = 'python'

print(letters[0], letters[2])

# 22

license_plate = "24가 2210"

print(license_plate[4:])

# 23

string = "홀짝홀짝홀짝"

print(string[::2])

# 24

string = "PYTHON"

print(string[: : -1 ])

# 25

phone_number = "010-1111-2222"

a = phone_number.replace("-", " ")

print( a )

# 26

phone_number = "010-1111-2222"

p_n = phone_number.replace("-","")

print( a )

##### 이렇게도 되나?

phone_number = "010-1111-2222"

 = phone_number.("-")

print( a ) # 안됨ㅠ


# 27

url = "http://sharebook.kr"

url_s = url.split(".")

print(url_s[1])

##### 이렇게도 되나?

url = "http://sharebook.kr"

print(url[ -2 ] + url[ -1 ]) # 된다!

# 28

lang = 'python'
lang[0] = 'P'
# print(lang) = 'python' cuz 문자열은 수정 불가능
print(lang)


# 29

string = 'abcdfe2a354a32a'
S = string.replace('a', 'A')
print( S )

# 30

string = 