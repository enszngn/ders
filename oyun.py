import random

sayi = random.randint(1,1000)

while True:
    tahmin = int(input('Tahmininiz: '))
    if tahmin == sayi:
        print('Tebrikler Bildiniz!')
        break
    elif tahmin > sayi:
        print('Daha kucuk.')
    else:
        print('Daha buyuk.')
print('Oyunu bitirdiniz.')
