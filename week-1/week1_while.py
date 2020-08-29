# while
# while <BOOLEAN EXPRESSION>:
# 		<LOOP BODY>
# else: (gawajib)
# 		<STATEMENTS>

# *note: kita harus pastiin ada kondisi suatu saat <BOOLEAN EXPRESSION> itu bernilai False
angka = 1

while angka <= 10:
    print(angka, end=" ")
    angka += 1
else:  # ini bakal keprint karena posisi terakhir si angka = 11, 11 <= 10 itu False
    print()
    print("selesai")

angka2 = 1
# break dan continue jg berlaku
print(50*"=")
while angka2 <= 3:
    print(angka2)
    if angka2 == 2:
        break
    angka2 += 1
else:  # dijalankan ketika <BOOLEAN EXPRESSION> nya salah
    print("selesai")