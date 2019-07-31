f1 = open('cash1.txt')
f2 = open('cash2.txt')
f3 = open('cash3.txt')
f4 = open('cash4.txt')
f5 = open('cash5.txt')
a = [[30, f1.readline().strip()]]
b = [[30, f2.readline().strip()]]
c = [[30, f3.readline().strip()]]
d = [[30, f4.readline().strip()]]
e = [[30, f5.readline().strip()]]
s = 0
index = 0
for i in range(15):
    a.append([30 + a[i][0], f1.readline().strip()])
    b.append([30 + b[i][0], f2.readline().strip()])
    c.append([30 + c[i][0], f3.readline().strip()])
    d.append([30 + d[i][0], f4.readline().strip()])
    e.append([30 + e[i][0], f5.readline().strip()])
    for j in range(1):
        if s < (float(a[i][1]) + float(e[i][1]) + float(d[i][1]) + float(c[i][1]) + float(b[i][1])):
            s = (float(a[i][1]) + float(e[i][1]) + float(d[i][1]) + float(c[i][1]) + float(b[i][1]))
            index = i

print(index + 1)
