def SelectSort1(nlist):
    size= len(nlist)
    cnt = 0

    for i in range(0, size-1, 1):
        for j in range(i+1, size, 1):

            if nlist[i] > nlist[j]:
                nlist[i] , nlist[j] = nlist[j], nlist[i]
                cnt += 1
        print("단계: ",i+1, datalist)

    print("총 데이터 교환 횟수:" , cnt)


datalist = [97,64,71,42,85,88]

print("선택정렬 1 오름차순")

print("선택정렬 before:", datalist)

SelectSort1(datalist)

print("선택정렬 after:", datalist)

