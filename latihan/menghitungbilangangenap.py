
n = int(input('\nMasukan bilangan genap \t\t\t: '))

count = 0

for i in range(0, n+1, 2):
    print(i, end=" ")
    count += 1

    
print('\nBilangan yang ditampilkan adalah : ', count)