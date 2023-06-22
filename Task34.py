stroka = input ("Введите стихотворение: ")
res = list(map(lambda x: x.count('-'), stroka.split()))
if res.count(res[0]) == len(res): print ("Рифма есть")
else: print ("Нет рифмы")


