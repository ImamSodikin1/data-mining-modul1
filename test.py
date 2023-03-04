print('Baris')
print('Identasi')

# tipe data
a = input('Masukan nilai A : ')
b = input('Masukan nilai B : ')


# percabangan if
angka = 4
if angka > 5:
    print(angka,'adalah bilangan positif')

# percabangan if else
bilangans = -1
if bilangans >= 0:
    print('Positif atau nol') 
else:
    print('Bilangan negatif')    

 # percabangan if elif else
bilang = 5.5

if bilang >= 0:
    print('Positif atau nol')
elif bilang == 0:
    print('Nol')    
else:
    print('Bilangan negatif')    

# if bersarang
gaji = 1_000_000

berkeluarga = True

punya_rumah = True

if gaji > 3_000_000:
    if berkeluarga:
        print('Wajib ikut asuransi dan menabung untuk pensiun')
    else:
        print('Tidak perlu ikut asuransi')    
    if punya_rumah:
        print('Wajib bayar pajak rumah')    
    else:
        print('Tidak wajib bayar pajak rumah')    
else:
    print('Gaji belum UMR')       


#  looping dengan for
nomor = [5,5,2]

jumlah = 0

for tampung in nomor:
    jumlah = jumlah + tampung
print('Jumlah semuanya : ', jumlah)  


# looping dengan range
for hitung in range(5):
    print('Hitung : ',hitung)



#  looping dengan while
hitung = 0

while (hitung < 5):
    print('Hitung : ', hitung)
    hitung += 1

    #  contoh program loping dengan while bilangan genap
i = 0
n = int(input('Masukan batas : '))

for i in range(n):
    if i%2 == 0:
        print('Bilangan : ', i)
    i += 1



#  function
def sapa(nama):
    print('hai, ' + nama + '. Apa kabar?')
    return nama

# memanggil function
sapa('Imam')


# contoh program hitun luas persegi panjang
def persegi_panjang(panjang,lebar):
    luas  = panjang * lebar
    print('Luas : ', luas)
    return luas

print('Masukan luas persegi panjang : ')
a = int(input('Masukan nilai panjang : '))
b = int(input('Masukan nilai lebar : '))

    # memanggil function luas persegi
persegi_panjang(a,b)    
   


