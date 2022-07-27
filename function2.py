def tambah (x) :
    hasil = x + 10
    return hasil

def kali (x) :
    hasil = x * 10
    return hasil

def minuman (x):
    y = str(x)
    hasil = y + ' susu'
    return hasil

daftar = []
for i in range (0,10):
    # y = tambah(i)
    y = kali(i)
    daftar.append(y)
    
print (daftar)
print (tambah(90))
print (minuman(10))