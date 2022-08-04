#fonksiyon
from distutils.log import fatal


def f(x):
    print(2*x)


def g(a):
    print(3*a)

def factoriel():
    print('hello world')
    f(2)
    print('hello world')
    f(3)
    print('hello world')
    f(10)
    print('hello world')

def f(x):
    return 2*x

cevap = f(2)
print(cevap)

def f(x, y):
    result = x + x * y - 1
    return result


    print(f(2, 3))
    print (f(2, 10))
    print(f(5, 10))

#parametre olarak 2 int alan, ve kucuk olani return eden, minimum adinda fonksiyon yaziniz.

def minimum(sayi1, sayi2):
    if sayi1 < sayi2:
        return sayi1
    else:
        return sayi2

print(minimum(5,10))
print(minimum(10,5))
print(minimum(5,5))
print(minimum(3,100))

#kullanicidan 2 adet int aliniz, ucuk olani minimum fonksiyonu ile ekrana basiniz.

def kucukolanibulma():
    sayi1 = int(input('1. sayiyi giriniz:  '))
    sayi2 = int(input('2. sayiyi giriniz:  '))
    print('kucuk sayi:', minimum(sayi1, sayi2))


def selamla(isim):
    print('Merhaba '+isim)

def merhaba():
    name=input('isminizi giriniz: ')
    print(selamla(name))


#parametre olarak bir sayi alan ve sayinin asal olup olmadigini anlayan bir fonksiyon yaziniz.

def isEven(number):
    if number % 2 == 0:
        return True
    else:
        return False

def isPrime(number):
    for i in range(2, number//2):
        if number % i == 0:
            return False

    return True
print(isPrime(21))

#isPrime metodunu kullanarak, 1500 ile 3000 arasindaki asal sayilari bulun.

def arasiasalsayi():
    for i in range(1500, 3000):
        if isPrime(i):
                print(i)

def piramid():
    sayi = int(input('bir sayi yaziniz: '))
    sayi3 = 0
    for i in range(sayi):
        if sayi3<sayi:
            sayi3=sayi3+1
            print('*'*sayi3)
        else:
            print('farkli bir sayi giriniz.')

def faktoriyel(sayi):
    cevap=1
    for i in range(1, sayi + 1):
        cevap *= (i+1)
    return cevap

import math

print(math.factorial(0))

#parametre olarak 2 sayi alip ortalamasini bulan fonksiyon(dogrulugunu test etmek icin 3 kere deneyiniz)

def ortalama(sayi1, sayi2):
    return ((sayi1+sayi2)/2)

print(ortalama(15, 25))
print(ortalama(150, 200))
print(ortalama(1, 2))

#parametre olarak bir sayi listesi alan ve ortalamasini return eden fonksiyon(3 deneme)

def listeortalama(list):
    return sum(list)/len(list)

print(listeortalama((1, 2, 3, 4, 5, 6)))
print(listeortalama((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))
print(listeortalama((100, 200, 300, 400 ,500)))

#kullanicidan input olarak liste alma yontem1:

def yontem1():
    liste = []
    while True:
        sayi4 = input('sayi giriniz: ')
        if sayi4 == '':
            break
    liste.append(int(sayi4))

    print(liste)

#kullanicidan input olarak liste alma yontem2:

def yontem2():
    liste2 = []
    uzunluk = int(input('liste uzunlugu:' ))
    for i in range(uzunluk):
        sayi5 = int(input('sayi giriniz: '))
        liste2.append(sayi5)

    print(liste2)

#kullanicidan input olarak liste alma yontem3:

def yontem3():
    liste3 = []
    str_list = input('liste giriniz: ')
    liste3 = str_list.split(' ')
    liste3 = (int(i) for i in liste3)
    print(liste3)

def factoriyel(n):
    cevap=1
    for i in range(1, n+1):
        cevap *= i

def maksimum(liste):
    return max(liste)

def maksimum1(liste):
    enbuyuk = liste[0]
    for i in liste:
        if i > enbuyuk:
            enbuyuk = i

    return enbuyuk

def maksimum2(liste):
    enbuyuk = liste[0]
    for i in liste:
        if i > enbuyuk:
            enbuyuk = i
    
    return enbuyuk

print(maksimum2((15, 26, 48 ,49 ,79 ,90, 2456, 456)))

def kelimeayirma():
    print('----------------------------------------------------')
    paragraf = input('metin giriniz: ')
    kelimeler = paragraf.split()
    for kelime in kelimeler:
        yenikelime = kelime[0].upper() + kelime[1:].lower()
        print(yenikelime, end='  ')
    print()
    print('----------------------------------------------------')

def examplerecursion(n):
    if n == 0:
        return
    print(n)
    examplerecursion(n-1)

examplerecursion(10)

print('---')

def examplerecursion(n):
    if n == 0:
        return
    print(n)
    examplerecursion(n-1)
    print(n)

examplerecursion(3)

"""

5! = 5 . 4!
4! = 4 . 3!
3! = 3 . 2!
2! = 2 . 1!
1! = 1 . 0!
n! = n . (n-1)!


"""


def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * factorial(n-1)


print(factorial(0))