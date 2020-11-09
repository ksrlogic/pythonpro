#2020314925 김승래

def BubbleSort(alist):
    size = len(alist)
    cnt = 0

    for i in range(size-1):

        for j in range(size-i-1):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
        
        print(i+1, "단계", alist)
        print('-'*30)
    print("총 데이터 교환 횟수: ", cnt)


datalist = [5,4,2,1,3]

print("버블정렬 오름차순")
print("버블정렬 before: ", datalist)

BubbleSort(datalist)
print("버블정렬 after: ", datalist)