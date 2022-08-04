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

for i in range(len(metin2)):
    print(i, metin2.find('a'))
sozcuk=input('metin giriniz: ')
sozcuk=sozcuk[0].upper()+sozcuk[1::].lower()
print(sozcuk)
sozcuk2 = input('sozcuk giriniz: ')
counter = 0
for i in range(len(sozcuk2)):
        if sozcuk2[i] == 'a':
                counter += 1
toplam=0
print(counter)
for i in range(5):
        number=input('bir sayi giriniz: ')
        toplam+=int(number)
print(toplam/5)
liste=(1,2,3,4,5,6,7,8,9,10)
print(liste[4])
print(liste[1::2])
print(liste[::2])

print(len(liste))
print(sum(liste))
print(max(liste))
print(min(liste))

#yukaridaki listenin ortalamasini print ediniz.
#yukaridaki listenin ilk yarisinin toplami ile son yarisinin toplaminin farkini print ediniz.
#yukaridaki listenin en buyuk ve kucuk sayisinin farkini print ediniz.

print(sum(liste)/len(liste))
print(max(liste)-min(liste))
ilkyarisi=liste[0:len(liste)//2:1]
sonyarisi=liste[len(liste)//2:len(liste):1]
print(sum(ilkyarisi)-sum(sonyarisi))
liste2 = [1,2,3,4,5,6,7,8,9,10]
liste3 = [97,98,99]
yeniliste=liste2+liste3
print(yeniliste)
print(list(range(20)))
print(list(range(10,20)))
print(list(range(10,20,2)))

#range metodu ile 0,100 arasindaki tum cift sayilari ekrana basiniz.
#range metodu ile 100,200 arasindaki tum tek sayilari ekrana basiniz.
#1000'den 0'a kadar 100'un katlarini tersten ekrana basiniz.

print(list(range(0,100,2)))
print(list(range(101,200,2)))
print(list(range(1000,0,-100)))

#0'dan 50'ye kadar, tum cift sayilarin, karesini ekrana basiniz.

for liste4 in range(0,51,2):
        print(liste4**2)
liste5 = [1, 2]
print(liste5)
liste5.append(10)
print(liste5)
liste5.insert(5,20)
print(liste5)
liste5.sort()
print(liste5)
print(liste5.pop())
print(liste5)
print(liste5.pop(0))

#insert kullanarak, append(99) yapiniz.

print(liste5)
liste5.insert(len(liste5),99)
print(liste5)
print(liste5)
liste5.reverse()
print(liste5)
liste6=(1,2,3,4,5)
yeniliste2=[]
for i in range(len(liste6)):
        yeniliste2.append(liste6[i]**2)
print(yeniliste2)
yeniliste2=[i**2 for i in liste6]
print(yeniliste2)
yasin=int(input('yasinizi giriniz: '))

if yasin<0 or yasin>120:
        print('yasiniz gecersiz.')
elif yasin>=0 and yasin <= 7:
        print('ilkokula gidiyorsun.')
elif yasin>=8 and yasin<=13:
        print('ortaokula gidiyorsun.')
elif yasin>=14 and yasin<=18:
        print('liseye gidiyorsun.')
elif yasin>=19 and yasin<=25:
        print('universiteye gidiyorsun.')
else:
        print('ise gidiyorsun.')
sayi2 = 0
while sayi2 < 100:
        print(sayi2)
        sayi2 = sayi2 + 2
        if sayi > 50:
                break

number2 = 0 
liste7 = []
while number2 != -1:
        number2 = int(input('bir sayi giriniz: '))
        if number2 != -1:
                liste7.append(number2)

print(liste7)
print(max(liste7))
print(min(liste7))
print(sum(liste7))
print(len(liste7))
print(sum(liste7) / len(liste7))