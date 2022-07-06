def sum(num1, num2):
    hap = num1 + num2
    return hap

def info(weight, height, **kwargs):
    print("키:", height)
    print("몸무게:", height)
    print("기타:", kwargs)

# 상수, 전역변수/ 눈에 잘 띄게 해서 사용에 유의하려고 대문자로 씀
# java는 final을 명시하면 해당 변수에 값을 한번만 입력할 수 있도록 정함
COMPANY = "파이썬 주식회사"

class Calculator:
    first = 0
    second = 0

    def __init__(self, first=None, second=None):
        self.first = first
        self.second = second

    def setData(self, first=None, second=None):
        self.first = first
        self.second = second

    def sum(self):
        return self.first + self.second

    def div(self):
        return self.first / self.second

    def mul(self):
        return self.first * self.second

    def sub(self):
        return self.first - self.second