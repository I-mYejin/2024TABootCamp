print("숫자 콤마 찍어주는 프로그램 :>")
cnt = 0

while True :
    X = input("20자리 이하의 수를 입력해주세요: ")
    if cnt == 3 :
        print("3번 틀렸습니다")
        break

    if X.isalpha() :
        print("숫자를 입력해주세요")
        continue

    if len(X) > 20 :
        print("20자리 이하의 숫자를 입력하시오")
        cnt += 1
        continue


# def comma(x) :
#     x = X.