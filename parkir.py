print ('1 = harian')
print ('2 = langganan')
parkir = input ('Masukkan tipe parkir = ')
pilihan = int (parkir)
print ('')
if pilihan == 1 :
    print ('Pilihan parkir anda adalah harian')
    print ('Perhitungan Parkir harian sebagai berikut :')
    print ('1 jam pertama = Rp3000')
    print ('Untuk jam berikutnya adalah Rp2000/jam')
    print ('Maksimal biaya parkir adalah Rp20000')
    print ('')
    jamparkir = input ('Masukkan lama parkir (jam) = ')
    biayawal = 3000
    lamaparkir = int (jamparkir)
    if lamaparkir < 2 :
        print ('Total lama parkir anda adalah ', jamparkir, "jam")
        print ('Biaya parkir anda adalah Rp', biayawal)
    elif lamaparkir <10 :
        biayaselanjutnya = (lamaparkir-1) * 2000 + biayawal
        print ('Total lama parkir anda adalah ', jamparkir, "jam")
        print ('Biaya parkir anda adalah Rp', biayaselanjutnya)
    else :
        print ('Total lama parkir anda adalah ', jamparkir, "jam")
        print ('Biaya parkir anda adalah Rp', 20000)
        
else :
    print ('Pilihan parkir anda adalah langganan')
    print ('Biaya satu kali parkir adalah Rp5000')
    print ('Sisa saldo anda adalah Rp45000')

# def main():
#     while True:
#         perulangan = input("Mau menggunakan program kembali ? [Y/N]")
        
#         if perulangan == 'n' :
#             print ('Terima kasih sudah menggunakan program parkir')
            
            
#         else :
#             print ('Yes')
#             if __name__ == "__main__":
#                 main()

            