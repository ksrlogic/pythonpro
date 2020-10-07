import random
while True:
    _list = []

    num = int(input("개수"))

    if num == 0 :
        break
    else:
        for x in range(num):
            msg = "%d/%d 번째 값을 입력하세요 :"%(x+1 ,num)
            num2 = random.randint(1,1000)
            print(msg, num2)
            _list.append(num2)

        min_num, max_num = -1, -1 #최소값과 최대값의 초기값 설정
        for i in range(len(_list)):
            cur_num = _list[i]
            if max_num < cur_num:
                max_num = cur_num
            if min_num == -1:
                min_num = cur_num
            elif min_num > cur_num:
                min_num = cur_num
        print("최소값 : %d 최대값: %d" %(min_num, max_num))