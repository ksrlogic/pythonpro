#Ex8-1_Sequential Search

print('학번 : 2020312463, 이름 : 문정인')
print('[순차 탐색]')

#순차 탐색 함수 정의

def SequentialSearch(key, slist):
    size = len(slist)

    for i in range(0,size,1): #range(size)
        if slist[i]==key:
            print('일치')
            return i
        else:
            print('불일치')
        
    return -1



#메인 코드
datalist=[5,4,2,1,3]
print('datalist의 데이터:', datalist)

key = int(input('탐색 키(search key) 입력:'))




#순차 탐색 함수 호출
index = SequentialSearch(key, datalist)

if index == -1:
    print('==>탐색 실패')
else:
    print('==>탐색 성공!!!')
    print('탐색 위치(index) = %d' %index)