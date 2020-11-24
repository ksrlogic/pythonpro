book_list = ['소설시', '에세이', '인문', '역사', '예술', '종교', '사회', '과학', '경제경영', '자기계발', '만화', '라이트노벨', '여행', '잡지', '어린이', '유아', '전집', '청소년', '요리', '육아' ]
index = -1

book_list.sort()
first = 0
last = len(book_list) - 1

print ( book_list )
target = int ( input ( "찾고자 하는 분야를 입력하세요 : " ) )

while first <= last :
    middle = ( first + last ) // 2
    if book_list[middle] == target :
        index = middle
        break
    elif book_list[middle] < target :    
        first = middle + 1
    else :     
        last = middle - 1

if index != -1 :
    print( target, "은 정렬된 분야의", middle, "번째 분야입니다." )
else :
    print( target, "은 존재하지 않는 분야입니다." ) 