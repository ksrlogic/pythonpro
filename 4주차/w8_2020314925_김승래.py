#도전과제 코드 추가

print("[도전w8] 학번 : 2020314925, 이름: 김승래")

print('[순차 탐색]')

list_data = [5,4,2,1,3,7,6]

print('리스트 데이터 : %s' % list_data)

key = input('탐색 키(search_key)압력 : ')

def search(slist, key):
    size = len(slist)
    
    for i in range(size):
        if(slist[i] == int(key)):
            print("%s 단계 %s == (slist[%s]=%s" %(i+1, key, i, slist[i]))
            print('=>%s회에 탐색 성공!!' % (i+1))
            print('=>탐색 위치(index) = %s' % i)
            break
        else:
            print("%s 단계 %s != (slist[%s]=%s" %(i+1, key, i, slist[i]))
    else:
        print('=> 탐색 실패')

search(list_data, key)