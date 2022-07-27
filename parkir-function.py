def harian (jam,tipe) :
    c = 0
    if tipe == 'mobil' :
        c = 2000 * jam
    elif tipe == 'motor' :
        c = 1000 * jam
    else :
        c = 0
    return c
    

def langganan (saldo):
    b = saldo - 5000
    return b

golongan = input ('golongan parkir = (harian/langganan)')
tipe = input ('Masukkan tipe kendaraan = (mobil/motor)')
if golongan == 'harian' :
    jamparkir = input ('berapa lama parkir = ')
    biayawal = 3000
    lamaparkir = int(jamparkir)
    ongkos = harian (lamaparkir,tipe)
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
    print ('Ongkos harian = {}'.format(ongkos))
    
elif golongan == 'langganan' :
    saldo = 50000
    saldoakhir = langganan(saldo)
    print ('Ongkos langganan = {}'.format(saldoakhir))