# 1. 입력한 금액을 5000원, 1000원, 500원, 100원으로 교환하는 프로그램
a = int(input())
a_5000 = a // 5000
a_1000 = (a % 5000) // 1000
a_500 = (a % 1000) // 500
a_100 = (a % 500) // 100
print(f'{a}원 교환 : {a_5000}개, {a_1000}개, {a_500}개, {a_100}개')