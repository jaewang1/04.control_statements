# 1. 사용자로부터 값을 입력
data = int(input("점수를 입력하세요.: "))

if 0 <= data <= 20 :
    print("e")
elif 21 <= data <= 40 :
    print("d")
elif 41 <= data <= 60 :
    print("c")
elif 61 <= data <= 80 :
    print("b")
elif 81 <= data <= 100 :
    print("a")
