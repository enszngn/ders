#sort

liste = [45, 76, 97, 15, 26, 35, 1, 2, 5, 6]
aranansayi = 3
bulduMu = False

for i in liste:
    if i == aranansayi:
        print('sayi bulundu!')
        bulduMu = True
        break

if not bulduMu:
    print('sayi bulunamadi!')

#bir listede, bir elemanin kac kere gectigini bulunuz ve print ediniz.

liste1= [123,43,2,43,42,4,24,23,42,4,23,42,34,234,24,3,3,3,3,3,3,3]
aranansayi = 3
count = 0
for i in liste1:
    if i == aranansayi:
        print('sayi bulundu!')
        count = count +1
if count == 0:
    print('sayi bulunamadi!')
else:
    print('sayi listede', count, 'defa bulundu!')

#parametre olarak bir liste ve bir sayi alan bir fonksiyon yaziniz ve bu fonksiyon liste icerisinde sayilarin kac kere gectigini bulup return etsin

def search(liste, sayi):
    counter=0
    for i in liste:
        if i == sayi:
            counter=counter+1
    return counter

liste2=[1,2,2,3,4,5,6,7,8,9,6,6,6,6,6,6]
print(search(liste2, 6))
print(search(liste2, 2))

#parametre olarak bir liste alan ve bu listeyi siralayip return eden bir fonksiyon yaziniz.

def sort(liste):
    yeniliste = []
    while len(liste)>0:
        enbuyuk = max(liste)
        yeniliste.append(enbuyuk)
        liste.remove(enbuyuk)
    return yeniliste


liste=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(sort(liste))