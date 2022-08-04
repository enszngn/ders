import datetime
print(list(range(0,100,7)))
sayi=int()
for i in range(14):
    sayi = sayi+7
    print(sayi)
start_time = datetime.datetime.now()
sayi2=int()
while sayi2 < 98:
    sayi2 = sayi2+7
    print(sayi2)
end_time = datetime.datetime.now()
print(end_time-start_time)