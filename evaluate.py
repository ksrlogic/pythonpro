sample = [[], [(450, 139), (600, 64), (675, 64), (825, 64), (900, 43)], [(650, 93)], [(450, 139), (600, 64), (675, 64), (750, 64)], [(500, 93)], [], []]
clistSample = [5.5, 4.5, 3.5 ,2.5 ,1.5]
score = 1000


# 50px 당 1시간



def competeOk(clist):
    checkList = []
    total = 0
    for i in range(len(clist)):
        weighted = clist[i] * (i * 1.2)
        checkList.append(weighted)
    for i in checkList:
        total += int(i)

    avg = total/len(checkList)

    if avg < 6.0:
        return "경쟁률 지수가 %s (으)로 적절합니다!" % avg
    else:
        return "경쟁률 지수가 %s (으)로 너무 높습니다!" % avg

def isEmpty(schedule):
    for i in range(0,5):
        if schedule[i] == []:
            global score
            score += 5
            return "쉬는 평일이 존재합니다. 좋아요!"
    else:
        return "쉬는 평일이 존재하지 않습니다. 하루 공강은 있는 편이 좋아요!"



DOTW = ["월", "화", "수", "목" , "금", "토", "일"]

def isTMclassEmpty(schedule):
    state = 0
    resultTexts = []
    for d in range(len(schedule)-1):
        day = schedule[d]
        for i in range(len(day)-1):
            if day == []:
                break
            tup = day[i]
            nextClass = day[i+1][0]
            block = tup[0] + tup[1]
            gongang = nextClass - block
            if gongang > 50 :
                resultTexts.append("%s요일 %d교시와 %d교시 사이에 너무 긴 공강이 존재합니다!" % (DOTW[d], i+1, i+2))
                state = 1
                global score
                score -= 5 # 5점 감점
                if gongang > 100:
                    score -= 5
                if gongang > 150:
                    score -= 5
                if gongang > 200:
                    score -= 5

    if state == 0 :
        resultTexts.append("긴 공강은 없어보입니다! 좋아요!")

    return resultTexts

def isMorning(schedule, weight):
    global score
    resultTexts = []
    for index, day in enumerate(schedule):
        if day == []:
            continue
        print(day)
        if int(day[0][0]) >= 450 and int(day[0][0]) < 550:
            weight = weight + 5 + 5 * weight
            score -= weight
            resultTexts.append("%s요일날 아침수업! 아침수업은 힘들어요!" % DOTW[index])
        elif day[0][0] >= 550 and day[0][0] < 650:
            weight = weight * 5
            score -= weight
            resultTexts.append("%s요일날 아침수업! 아침수업은 힘들어요!" % DOTW[index])
        else:
            continue

    return resultTexts

def TMClassContinue(schedule):
    resultTexts = []
    global score
    for i, day in enumerate(schedule):
        ContinueCnt = 0
        if day == []:
            continue
        for  index ,_class in enumerate(day):
            block = _class[0] + _class[1]
            cnt = len(day)
            while cnt - index > 1:
                # [[], [(450, 139), (600, 64), (675, 64), (825, 64), (900, 43)], [(650, 93)], [(450, 139), (600, 64), (675, 64), (750, 64)], [(500, 93)], [], []]
                nextClass = day[index + 1][0]
                if nextClass - block < 30:
                    ContinueCnt +=1
                    print(ContinueCnt)
                break

        if ContinueCnt > 2:
            
            score -= 5
            resultTexts.append("%s요일날 연강이 너무 많습니다!" % DOTW[i])
    
    return resultTexts

print(TMClassContinue(sample))
print(isMorning(sample,1))
print(score)
def evaluate(schedule, weight):
    isEmpty(schedule)
    isTMclassEmpty(schedule)
    isMorning(schedule, weight)



