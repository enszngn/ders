#class
from time import perf_counter


class Personel():
    def __init__(self, isim):
        self.isim = isim

    def selamla(self):
        print('Merhaba', self.isim)


per1 = Personel('Ahmet')
per2 = Personel('Ayse')
per3 = Personel('Enes')
