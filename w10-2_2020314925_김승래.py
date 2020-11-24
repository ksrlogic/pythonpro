print("[도전w10-2] 학번:2020314925, 이름:김승래")
print("[이진 탐색(오름차순 정렬)]")
numlist = [72, 88, 10, 15, 46, 49, 78, 94, 54, 32, 19, 18, 71]

def BinarySearchDESC(skey, slist):
    global cnt
    cnt = 1
    low = 0
    high = len(slist) - 1
    while low<=high:
        mid = (low + high) // 2 
        print("%d 단계, key=%s, data[%s]=%s =>"% (cnt, skey, mid, slist[mid]), end="")
        if skey > slist[mid]:
            high = mid - 1
            print("불일치")
        elif skey < slist[mid]:
            low = mid + 1
            print("불일치")
        else:
            print("일치")
            return mid
        cnt += 1
    return -1
def BinarySearchUP(skey, slist):
    global cnt
    cnt = 1
    low = 0
    high = len(slist) - 1
    while low<=high:
        mid = (low + high) // 2 
        print("%d 단계, key=%s, data[%s]=%s =>"% (cnt, skey, mid, slist[mid]), end="")
        if skey < slist[mid]:
            high = mid - 1
            print("불일치")
        elif skey > slist[mid]:
            low = mid + 1
            print("불일치")
        else:
            print("일치")
            return mid
        cnt += 1
    return -1

print("Data: ", numlist)

while 1 :
    choice = int(input("오름차순: 1, 내림차순: 2 => "))
    if choice == 1:
        numlist.sort(reverse=False)
        print("SortedData: ", numlist)
        skey = int(input("탐색 키 입력: "))
        result = BinarySearchUP(skey, numlist)
        break
    elif choice == 2:
        numlist.sort(reverse=True)
        print("SortedData: ", numlist)
        skey = int(input("탐색 키 입력: "))
        result = BinarySearchDESC(skey, numlist)
        break
    else:
        print('다시 입력해주세요!')
    

if result == -1:
    print("=> 탐색실패")
else:
    print("=>탐색 성공!!!", cnt, "회 탐색")
    print("=>탐색 위치(index)=" , result)