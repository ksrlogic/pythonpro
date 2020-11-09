print("[도전w8] 학번 : 2020314925, 이름: 김승래")

print('[순차 탐색]')

list_data = [5,4,2,1,3,7,6]

print('리스트 데이터 : %s' % list_data)

key = input('탐색 키(search_key)압력 : ')

def search(slist, key):
    size = len(slist)
    
    for i in range(size):
        print('%d 단계 %s와(과) 인덱스 %d번째의 값 %s 비교 =>'% (i+1, key, i, slist[i]) ,end="")
        if(slist[i] == int(key)):
            print(' 일치')
            print('=>%s회에 탐색 성공!!' % (i+1))
            print('=>탐색 위치(index) = %s' % i)
            break
        else:
            print(' 불일치')
    else:
        print('=> 탐색 실패')

search(list_data, key)           