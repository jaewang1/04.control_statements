# # 1. 사용자로부터 값을 입력 받은 후(문자열)
# num = input("임의의 숫자를 입력하세요.: ")
# # 2. 해당 값에 100을 더한 값을 계산(숫자형)
# num_2 = int(num) + 100
# # 3. 계산한 값이 150 초과인 경우 출력, 150 이하인 경우 '값이 부족합니다' 출력
# if num_2 > 150 :
#     print(num_2)
# elif num_2 <= 150 :
#     print("값이 부족합니다.")
#

# 사용자로부터 임의의 숫자를 입력 받아
data = input("숫자를 입력하세요.: ")
data_2 = int(data)
# 해당 수가 5와 10 사이에 있으면 'ok', 그렇지 않으면 'no' 출력
if 5 < data_2 < 10 :
    print("ok")
else :
    print("no")

