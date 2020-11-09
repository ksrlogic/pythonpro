print("[도전w9] 학번 : 2020314925, 이름: 김승래")

pstr = "WHEN I FIND MYSELF IN TIMES OF TROUBLE"

pattern = "FIND"

print("주여진 문자열: ", pstr)
print("찾고자 하는 패턴 :", pattern)
print()

ssize = len(pstr)
psize = len(pattern)

i = 0
cnt = 0

while i<ssize:
    t_pstr = pstr[i:]

    if pattern in t_pstr:
        t_index = t_pstr.index(pattern)
        print(pstr.index(pattern))

        print("Matched index: ", i+t_index)
        cnt += 1
        i = i + t_index + 1
    else:
        break

if cnt == 0 :
    print("No index Matched")

print("Finish!")