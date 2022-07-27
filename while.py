buah = ['mangga', 'apel', 'jeruk', 'pepaya', 'rambutan', 'durian']
i = len (buah)
a = -1
while a < i-1 :
    a = a + 1
    if a == 4 :
        continue
    print (buah[a])
else :
    buah.append('nanas')

print (buah)