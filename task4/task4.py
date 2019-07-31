f = open("data.txt")        # Код шероховатый, но рабочий.
x = f.readlines()
list1 = []
list2 = []
inter = []
b = []
for i in range(720):        # Здесь я создаю массив со всеми минутами рабочего дня(12 часов = 720 минут), со вторым слотомй
    b.append([i, 0])        # для учета количества посетителей в конкретную минуту

for i in range(len(x)):             # Тут в силу моей неопытности данные, скопированные из файла перенеслись криво
    list1 += list(x[i].split("\n")) # Поэтому я подчистил их во время переноса в новый массив
    if '' in list1:
        list1.remove('')

for i in range(len(list1)):             # В этом цикле я перевожу время из формата "19:00" в минуты 
    ss = list1[i].split(' ')            # Чтобы потом можно было их совместить с массивом b
    sss1 = ss[0].split(":")
    sss2 = ss[1].split(":")
    list2.append([(int(sss1[0]) - 8)*60 + int(sss1[1]), (int(sss2[0]) - 8)*60 + int(sss2[1])])  # Диапазон вношу в массив list2

for i in range(len(list2)):                     # В этом цикле сверяю все минуты в диапазоне входа/выхода каждого посетителя
    for j in range(list2[i][0], list2[i][1]):   # и при совпадении добавляю добавляю единицу во второй слот массива b
        if j == b[j][0]:
            b[j][1] += 1

m = b[0][1]
for i in range(len(b)):             # Выявляю максимальное количество посетителей
    if b[i][1] > m:
        m = b[i][1]
for i in range(len(b)):             # Выявляю минуты с максимальным количеством посетителей и вношу их в отдельный массив
    if b[i][1] == m:
        inter.append(b[i][0])

start = inter[0]                        # Соглашусь, эта часть задачи выглядит как чернобыльский мутант, но тем не менее
end = 0                                 # оно способно выводить не округленное время "19:45", а даже, например, "19:48" !
for i in range(len(inter)):             
    if (inter[i] - inter[i - 1]) > 1:   # В моем распоряжении сплошной массив, где периоды посещений не разделены
        end = inter[i - 1]              # поэтому я стал выявлять их, сравнивая разность рядом стоящих элементов
        a1 = (start // 60) + 8          # из большего вычитал меньшее и если эта разность составляла больше единицы
        a2 = start % 60                 # То это означает, что период кончился и приписываю переменной end предыдущий элемент
        if a2 == 0:                     # Таким образом я получаю выцеженный период с минутами, который потом перевожу часы
            a2 = "00"
        a3 = ((end + 1)//60) + 8
        a4 = (end + 1) % 60
        if a4 == 0:                     # Так же я столкнулся с такой неприятностью, что если во второй половине числа получался ноль
            a4 = "00"                   # То на выход получалось некрасивое время, а именно "9:0", вместо "9:00"
        print(str(a1) + ":" + str(a2) + " " + str(a3) + ":" + str(a4))
        start = inter[i]
a1 = (start // 60) + 8                  # Красиво выйти из цикла у меня не получилось, поэтому последний период высчитывается уже после 
a2 = start % 60
if a2 == 0:
    a2 = "00"
a3 = ((inter[-1] + 1)//60) + 8
a4 = (inter[-1] + 1) % 60
if a4 == 0:
    a4 = "00"
print(str(a1) + ":" + str(a2) + " " + str(a3) + ":" + str(a4))
