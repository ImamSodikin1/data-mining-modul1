

def persegi_panjang(panjang,lebar):
    luas = panjang * lebar
    print('Luas\t\t: ', luas)

    sisi = int(input('\nMasukan sisi\t: '))
    luas -= sisi
    print('Luas\t\t: ', luas,'\n')
    return luas

panjang = int(input('\nMasukan panjang\t: '))

lebar   = int(input('Masukan lebar\t: '))

# memanggil function 
persegi_panjang(panjang,lebar)