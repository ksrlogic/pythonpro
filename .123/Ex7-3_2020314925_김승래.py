def SelectSort2(nlist):
    size= len(nlist)
    cnt = 0

    for i in range(size-1):
        minindex = i
        for j in range(i+1, size):
            if nlist[minindex] > nlist[j]:
                minindex = j
        if minindex != i :
            nlist[i], nlist[minindex] = nlist[minindex], nlist[i]
            cnt += 1
        print("단계: ",datalist)

    print("총 데이터 교환 횟수:" , cnt)


datalist = [97,64,71,42,85,88]

print("선택정렬 2 오름차순")

print("선택정렬 before:", datalist)

SelectSort2(datalist)

print("선택정렬 after:", datalist)