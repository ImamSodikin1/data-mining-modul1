
# Latihan menghitung karakter tanpa spasi
def count_char_without_space(string):
    count = 0
    for char in string:
        if char != " ":
            count += 1
    return count

# Masukan nama
string = input("\nNama\t\t\t: ")

jumlah_karakter = count_char_without_space(string)

print("Jumlah karakter Nama\t:", jumlah_karakter,"\n")

# Masukan NIM
string = input("NIM\t\t\t: ")

jumlah_karakter = count_char_without_space(string)

print("Jumlah karakter NIM\t:", jumlah_karakter,"\n")
