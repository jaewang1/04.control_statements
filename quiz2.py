# 사용자로부터 입력 받은 단어가 아래 fruit 리스트에 포함되어 있는지 확인
# text = input("조회할 요소를 입력하세요: ")
# fruit = ["사과", "포도", "홍시"]
# # 포함되어 있다면 '정답입니다', 아닐 경우 '오답입니다' 출력
# if text in fruit :
#     print("정답입니다.")
# else :
#     print("오답입니다.")

# list = []
# dic =  {}
text = input("조회할 요소를 입력하세요: ")
dic = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
if text in dic :
    print("정답입니다.")
else :
    print("오답입니다.")


