# 숫자형 - 정수형
a = 123
print(type(a))

# 숫자형 - 실수형
a = 1.2
b = -3.42
c = 4.24E10
print(type(a))
print(type(b))
print(type(c))

# 숫자형 - 8진수와 10진수
a = 0o177
b = 0xABC
print(type(a))
print(a)
print(type(b))
print(b)

# 숫자형 - 사칙연산
a = 3
b = 7
print(a + b) # 더하기
print(a - b) # 뺄셈
print(a * b) # 곱하기
print(a / b) # 나누기
print(a // b) # 몫 구하기
print(a % b) # 나머지 구하기
print(a ** b) # 제곱

# 문자형
a = """Life is too short, you need Python"""
print(a)
b = """Life" is too short, you need Python"""
print(b)
c = "Life is too short, you need Python"
print(c)
d = 'Life" is too short, you need Python'
print(d)
e = 'Life\'s too short, you need Python'
print(e)
f = 'Life is too short,\n you need Python'
print(f)
g = '''Life is too short,
you need Python'''
print(g)

# 문자형 - 연산하기
head = "Python"
tail = " is good"
print(head + tail)

delimeter = "=" * 50
print(delimeter)
print('hello_world')
print(delimeter)

a = "Hello World"
# 문자형 - 길이구하기
print(len(a))

# 문자형 - 인덱스 활용하기
print(a[3])
print(a[-3])

# 문자형 - 자르기
print(a[0:5])
print(a[0::])
print(a[::-1])