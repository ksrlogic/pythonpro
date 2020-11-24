print("[도전w10-1] 학번:2020314925, 이름:김승래")
print("[이진 탐색(오름차순 정렬)]")
numlist = [72, 88, 10, 15, 46, 49, 78, 94, 54, 32, 19, 18, 71]

def BinarySearchASC(skey, slist):
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

print("Data: ", numlist)

numlist.sort(reverse=True)

print("SortedData: ", numlist)

skey = int(input("탐색 키 입력: "))

result = BinarySearchASC(skey, numlist)

if result == -1:
    print("=> 탐색실패")
else:
    print("=>탐색 성공!!!", cnt, "회 탐색")
    print("=>탐색 위치(index)=" , result)