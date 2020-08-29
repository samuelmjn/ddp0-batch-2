# n = 3, 3 baris
# ...*
# ..***
# .*****
# *******

# Wafi
n = int(input("Piramida berapakah yang anda inginkan? "))

print()
    #setangah bintang
for i in range(1, n+1):
    print("*" * i)

print()
    #jumlah bintang terakhir
s = n//2
for i in range(1, n+1, 2):
    print (" " * s + "*" * i)
    s -= 1

print()
    #jumlah baris bintang
a = 1+(2*(n-1))
s = a//2
for i in range(1, a+1, 2):

    print (" " * s + "*" * i)
    s -= 1

print()

# Dimas
baris = int(input("Masukkan jumlah bintang terakhir (angka ganjil): "))
base = baris//2+1

if ((baris <= 0) or (baris % 2 == 0)):
    print("Masukkan angka yang benar!")
else:
    jarak = baris//2
    bintang = 1
    while (base <= baris):
        print(" " * jarak + "*" * bintang)
        bintang += 2
        jarak -= 1
        base += 1
    else: print("Done!")