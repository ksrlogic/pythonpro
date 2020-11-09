#2020314925 김승래 9주차

pstr = "WHEN I FIND MY SELF IN TIMES OF TROUBLE"

pattern = "TROUBLE"

print("주여진 문자열: ", pstr)
print("찾고자 하는 패턴 :", pattern)
print()

ssize = len(pstr)
psize = len(pattern)

for i in range(ssize):

    if len( pstr[i:]) < psize:
        print("Finish!!!")
        break
    cnt = 0
    for j in range(psize):
        if pstr[i+j] == pattern[j]:
            cnt += 1

    if cnt == psize:
        print("Matched Index: ", i)
    