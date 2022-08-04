#sezar sifresi
def sezarsifre(text, sayi):
    newtext = ''
    for i in text:
        newtext = newtext + chr(ord(i)+ sayi)
    return newtext
print(sezarsifre('merhaba', 3))