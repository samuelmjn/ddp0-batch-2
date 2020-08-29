# cara dapetin angka random
# import random

# angka = random.randint(1,10)
# print(angka)

# Looping
# User Input
# Branching

import random

# DIMAS POENYA
salah = 0

angka = random.randint(1, 10)
while (salah < 3):
    jawaban = int(input("Masukkan angka 1 nomor:"))
    # ingat input itu return nya string
    if (jawaban == angka):
        print("jawabanmu benar")
        break
    else:
        print("jawabanmu salah")
        salah += 1
    print("sisa nyawa kamu ", 3-salah)


# Wafi
ans1 = random.randint(1, 10)
n = 3

while n > 0:
    uinput = input("Coba tebak! Berapakah angka yang saya miliki: ")

    if (int(uinput) == ans1):
        print("Hebat! Tebakan Anda Benar")
        break
    else: 
        print("Salah! Coba Lagi!")
        n -= 1
        print("Sisa kesempatan anda =", end=" ")
        print(n)
        continue
else:
    print("Sayang Sekali! Kesempatanmu sudah habis!")


# Aiko
import random

jawaban = random.randint(1,10)

jumlah_percobaan = 0

while jumlah_percobaan < 3:
    tebakan = input('Masukkan tebakan angka 1-10: ')
    if int(tebakan) != jawaban:
        print('Yah, tebakannya salah..')
    else:
        print('Selamat, tebakannya benar!')
        break
    jumlah_percobaan += 1
else:
    print('Kesempatannya udah abis, coba lagi nanti ya!')