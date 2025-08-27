print("Masukkan elemen matriks A (3x3):")
matriks_a = []
for i in range(3):
    baris = []
    for j in range(3):
        data = int(input("A[" + str(i+1) + "," + str(j+1) + "] = "))
        baris = baris + [data]
    matriks_a = matriks_a + [baris]

print("\nMasukkan elemen matriks B (3x3):")
matriks_b = []
for i in range(3):
    baris = []
    for j in range(3):
        data = int(input("B[" + str(i+1) + "," + str(j+1) + "] = "))
        baris = baris + [data]
    matriks_b = matriks_b + [baris]

print("\nPilihan Menu :")
print("1. Penjumlahan matriks A + matriks B")
print("2. Pengurangan matriks A - matriks B")
print("3. Perkalian matriks A x matriks B")
print("4. Cek matriks A dan B = matriks satuan ?")
pilihan = int(input("Masukkan pilihan: "))

if pilihan == 1:
    print("\nHasil Penjumlahan A + B:")
    for i in range(3):
        for j in range(3):
            print(matriks_a[i][j] + matriks_b[i][j], end=" ")
        print()

elif pilihan == 2:
    print("\nHasil Pengurangan A - B:")
    for i in range(3):
        for j in range(3):
            print(matriks_a[i][j] - matriks_b[i][j], end=" ")
        print()

elif pilihan == 3:
    print("\nHasil Perkalian A x B:")
    matriks_c = []
    for i in range(3):
        baris = []
        for j in range(3):
            total = 0
            for k in range(3):
                total = total + matriks_a[i][k] * matriks_b[k][j]
            baris = baris + [total]
        matriks_c = matriks_c + [baris]
    for i in range(3):
        for j in range(3):
            print(matriks_c[i][j], end=" ")
        print()

elif pilihan == 4:
    cek_matriks_a = True
    for i in range(3):
        for j in range(3):
            if matriks_a[i][j] != 0 and matriks_a[i][j] != 1:
                cek_matriks_a = False
    if cek_matriks_a:
        print("Matriks A adalah matriks satuan")
    else:
        print("Matriks A bukan matriks satuan")

    cek_matriks_b = True
    for i in range(3):
        for j in range(3):
            if matriks_b[i][j] != 0 and matriks_b[i][j] != 1:
                cek_matriks_b = False
    if cek_matriks_b:
        print("Matriks B adalah matriks satuan")
    else:
        print("Matriks B bukan matriks satuan")

else:
    print("Bukan pilihan yang benar")
