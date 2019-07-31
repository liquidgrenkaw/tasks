f = open("data.txt")
x = f.readlines()
list1 = []
list2 = []
inter = []
b = []
for i in range(720):
    b.append([i, 0])

for i in range(len(x)):
    list1 += list(x[i].split("\n"))
    if '' in list1:
        list1.remove('')

for i in range(len(list1)):
    ss = list1[i].split(' ')
    sss1 = ss[0].split(":")
    sss2 = ss[1].split(":")
    list2.append([(int(sss1[0]) - 8)*60 + int(sss1[1]), (int(sss2[0]) - 8)*60 + int(sss2[1])])

for i in range(len(list2)):
    for j in range(list2[i][0], list2[i][1]):
        if j == b[j][0]:
            b[j][1] += 1

m = b[0][1]
for i in range(len(b)):
    if b[i][1] > m:
        m = b[i][1]
for i in range(len(b)):
    if b[i][1] == m:
        inter.append(b[i][0])

start = inter[0]
end = 0
for i in range(len(inter)):
    if (inter[i] - inter[i - 1]) > 1:
        end = inter[i - 1]
        a1 = (start // 60) + 8
        a2 = start % 60
        if a2 == 0:
            a2 = "00"
        a3 = ((end + 1)//60) + 8
        a4 = (end + 1) % 60
        if a4 == 0:
            a4 = "00"
        print(str(a1) + ":" + str(a2) + " " + str(a3) + ":" + str(a4))
        start = inter[i]
a1 = (start // 60) + 8
a2 = start % 60
if a2 == 0:
    a2 = "00"
a3 = ((inter[-1] + 1)//60) + 8
a4 = (inter[-1] + 1) % 60
if a4 == 0:
    a4 = "00"
print(str(a1) + ":" + str(a2) + " " + str(a3) + ":" + str(a4))
