# a = "이재왕"
# b = "이관훈"
#
# if a != b :
#     print("두 사람의 이름은 다릅니다.")
# elif a != b :
#     print("두 사람의 이름은 다릅니다.")
#
#
# num_1 = 10
# num_2 = 3
#
# if num_1 < num_2 :
#     print("num_1은 num_2보다 크기가 작습니다.")
#
# elif num_1 == num_2 :
#     print("num_1은 num_2보다 크기가 같습니다.")
#
# elif num_1 > num_2 :
#     print("num_1은 num_2보다 크기가 큽니다.")

# 1. 사용자로부터 값을 입력 받은 후(문자열)
num = input("임의의 숫자를 입력하세요.: ")
# 2. 해당 값에 100을 더한 값을 계산(숫자형)
num_2 = int(num) + 100
# 3. 계산한 값이 150 초과인 경우 출력, 150 이하인 경우 '값이 부족합니다' 출력
if num_2 > 150 :
    print(num_2)
elif num_2 <= 150 :
    print("값이 부족합니다.")


