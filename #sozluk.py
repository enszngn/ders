#sozluk
sozluk={
    'beyaz':'white',
    'kirmizi':'red',
    'siyah':'black'
}
print(sozluk('beyaz'))
print(sozluk.keys())
print(sozluk.values())
print(sozluk.items())

for key, value in sozluk.items():
    print(key.value)

sozluk['mavi'] = ['blue']
