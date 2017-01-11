class OutOfRangeError(Exception):
    pass

def inputDan():
    try:
        dan = int(input("몇 단을 출력 하시겠습니까?"))

        if dan > 1 and dan < 10:
            for num in range(1, 10):
                print("{} * {} = {}".format(dan, num, dan * num))
        else:
            raise OutOfRangeError

    except:
        print("2에서 9사이의 숫자만 입력해주세요.")
        inputDan()

inputDan()



