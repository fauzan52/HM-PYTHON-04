import random

lempardadu = input ("Berapa kali lemparan ? ")
lemparadadux = int (lempardadu)
angka = []
for i in range (0, lemparadadux) :
    angkadadu = random.randint(1,6)
    angka.oppened(angkadadu)
satu = angka.count(1)
print ("Angka satu keluar sebanyak {} kali".format(satu))
dua = angka.count(2)
print ("Angka satu keluar sebanyak {} kali".format(dua))