
yazi = 1234
print(yazi)
ornek_bool = True
print(ornek_bool, type(ornek_bool))
metin = 'merhaba'
print(metin, type(metin))
print(30/16)
print(15+15/2**3)
print(5==5)
print(5==7)
print(3<=3)
sayi = 1
sayi = sayi + 1
print(sayi)
gelir = input('Gelirinizi giriniz : ')
gelir = int(gelir)
vergi_yuzdesi = 0.18
vergi = gelir * vergi_yuzdesi 
print('Verginiz', vergi)
metin2 = 'merhaba dunya'
print(metin)
print(type(metin))
metin3 = 'merhaba \ndunya'
print(metin3)
print(len(metin))
print(metin.upper())
print(metin[0])
print(metin[1])
print(metin[6])
print(metin[-1])
print(metin[-6])
print(metin2[0:7])
print(0)
print(metin2[8:len(metin2)])
metin4 = 'm-e-r-h-a-b-a- -d-u-n-y-a'
print(metin4[0 : len(metin4) : 2])
metin5 = input("metin giriniz: ")
print(metin5[0:len(metin5):2])
print(metin5[::2])
print(metin5[0 : : 2])
print(metin2[::-1])
a = int(input("1 den 10'a kadar bir sayi giriniz: "))
if a < 5:
        print("a 5'den kucuk")
elif a == 5:
        print("a 5'e esit")
else:
        print("a 5'den buyuk")
for i in range(15):
        print(i)
yaslar_toplami = 0
for i in range(3):
    dogum_tarihi=input("dogum tarihinizi giriniz: ")
    yaslar_toplami += 2022 - int(dogum_tarihi)
print(yaslar_toplami/3)
metin2 = 'n' + metin[1:]
metin2 = metin2[:-1] + 'e'
metin2 = "merhaba dunya"
print(metin2)
print(metin2.upper())
print(metin2.lower())
print(metin2.capitalize())
print(metin2.title())
print(metin2.swapcase())
print(metin2.count('a'))
print(metin2.find('a'))

#bir metindeki 'a' karakter sayisini for loop ile bulunuz.
#kullanicidan 5 adet sayi aliniz ve ortalamasini ekrana yaziniz.
#input olarak bir metin alan, ve title metodunu kullanmadan title haline ceviren kodu yaziniz. (upper lower ile)

for i in range(13):
    print(i, metin2[1])
