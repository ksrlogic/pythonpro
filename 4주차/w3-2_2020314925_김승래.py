N = int(input())

bigArray = []
secondArray = []

for i in range(0,N):
    bigArray.append([])
    secondArray.append([])
    for j in range(0,N):
        a= int(input())
        bigArray[i].append(a)
        secondArray[i].append(a*i*j)
print(bigArray)
print(secondArray)


