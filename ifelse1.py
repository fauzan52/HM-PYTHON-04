minuman = input ("Masukkan minuman anda : ")
minumanku = minuman.strip().replace(' ', ' ')
if minumanku == 'kopi' :
    print ('sama')
elif minumanku == 'susu' :
    print ('minum susu itu sehat')
else :
    print ('Minum {} yaa.' .format(minuman))