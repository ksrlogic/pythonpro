sample = [[], [(450, 139), (600, 64), (675, 64), (825, 64), (900, 43)], [(650, 93)], [(450, 139), (600, 64), (675, 64), (750, 64)], [(500, 93)], [], []]

def isEmpty(schedule):
    for i in range(0,5):
        if schedule[i] == []:
            print("쉬는 평일이 존재합니다. 좋아요!")
            break
    else:
        print("쉬는 평일이 존재하지 않습니다. 하루 공강은 있는 편이 좋아요!")



DOTW = ["월", "화", "수", "목" , "금", "토", "일"]

def isTMclassEmpty(schedule):
    state = 0
    for d in range(len(schedule)-1):
        day = schedule[d]
        for i in range(len(day)-1):
            if day == []:
                break
            tup = day[i]
            nextClass = day[i+1][0]
            block = tup[0] + tup[1]
            if nextClass - block > 150 :
                print("%s요일 %d교시와 %d교시 사이에 너무 긴 공강이 존재합니다!" % (DOTW[d], i+1, i+2))
                state = 1
    if state == 0 :
        print("긴 공강은 없어보입니다! 좋아요!")



def evaluate(schedule):
    isEmpty(schedule)
    isTMclassEmpty(schedule)