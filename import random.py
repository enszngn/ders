import random
isim = input('isminizi yaziniz: ')
isim = isim.lower() + isim.upper() + '1234567890'
sifre = ''
for i in range (10):
    sifre = sifre + random.choice(isim)
print(sifre)
