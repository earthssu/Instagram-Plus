# if answer >= 5:
#     print(" 0, 1, 2, 3 중 하나의 숫자를 입력해주세요 ")

print(" 거주하는 지역의 구를 입력해주세요. ex)서초구 ")
adr = str(input())
print()

print(" 지금부터 코로나 우울증 검사를 시작하겠습니다. ")
print(" 점수표를 참고하여 점수를 입력해주시면 됩니다. ")
print()
print(" 없음 - 0, 가끔 - 1, 자주 - 2, 거의매일 - 3 ")
print()
print()
print()


num1 = int(input(" 1. 기분이 가라앉거나 우울하고, 희망이 없다고 느꼈다. "))
while True :
    if num1 == 0 or num1 == 1 or num1 == 2 or num1 == 3: break
    print(" 0, 1, 2, 3 중 하나의 숫자를 입력해주세요 ")
    num1 =int(input(" 1. 기분이 가라앉거나 우울하고, 희망이 없다고 느꼈다. "))



print()
num2 = int(input(" 2. 평소하던 일에 대한 흥미가 없어지거나 즐거움을 느끼지 못했다. "))
print()
num3 = int(input(" 3. 잠들기가 어렵거나 자주 깼다.(혹은 너무 많이 잔다.) "))
print()

# answer = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9
#
# print(" 당신의 우울증 점수는... %d점 입니다. " % (answer))
# print()