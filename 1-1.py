print('''
===========도형 목록=============
1. 원
2. 삼각형
3. 직사각형
4. 정사각형
================================
''')

pi = 3.1415

def circle():
    r = int(input("원의 반지름을 입력해주세요: "))
    s = r**2*pi
    print(f"반지름이 {r}인 원의 넓이는 {s:.2f}입니다.")

def triangle():
    a = int(input("삼각형 밑변 길이를 입력해주세요: "))
    b = int(input("삼각형 높이 길이를 입력해주세요: "))
    print(f"밑변이 {a}이고 높이가 {b}인 삼각형의 넓이는 {(a*b)/2}입니다.")

def rectangle():
    a = int(input("직사각형 가로 길이를 입력해주세요: "))
    b = int(input("직사각형 세로 길이를 입력해주세요: "))
    print(f"가로가 {a}이고 세로가 {b}인 직사각형의 넓이는 {a*b}입니다.")

def square():
    a = int(input("정사각형 한 변의 길이를 입력해주세요: "))
    print(f"한 변의 길이가 {a}인 정사각형의 넓이는 {a*a}입니다.")

while True:
    num = int(input("도형 목록에서 넓이를 계산할 도형의 번호를 입력해주세요: "))
    if num == 1:
        circle()
        break
    elif num == 2:
        triangle()
        break
    elif num == 3:
        rectangle()
        break
    elif num == 4:
        square()
        break
    else:
        print("도형 목록에 제시된 번호와 일치하지 않습니다. 다시 입력하세요")
        continue