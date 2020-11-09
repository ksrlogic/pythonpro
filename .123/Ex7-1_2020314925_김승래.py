def insertSort(nlist):
    size = len(nlist)

    for i in range(1, size):
        indata = nlist[i]
        pos = i

        while pos > 0 and nlist[pos-1] > indata:
            nlist[pos] = nlist[pos - 1]
            pos -= 1
        if pos != i:
            nlist[pos] = indata

        print(i, '단계:', nlist)
        print('-'*30)

datalist = [97,64,71,42,85,88]
print("삽입정렬 오름차순")

print("삽입정렬 before:" , datalist)

insertSort(datalist)

print("삽입정렬 after:", datalist)