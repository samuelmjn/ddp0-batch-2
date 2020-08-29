# for else

for i in range(6):
    print(i)
else:  # akan dieksekusi setelah semua proses for selesai
    print("selese")

# break dan continue dalam loop
# break: interupsi proses for/ keluar atau berhenti dari for secara paksa

for i in range(10000):
    print(i)
    if i == 4:
        break
else:
    print("selesai")  

# ini ga diprint karena proses for tidak selesai semuanya
    # ketika i == 4 proses sudah selesai secara paksa karena break

print('-'*50)
# continue: men-skip satu iterasi
for i in range(11):
    if i % 2 == 0:
        continue  
    # kode di bawah tidak dieksekusi jika masuk ke continue
    print(i)

# kode di bawah continue tidak dieksekusi dan langsung skip ke iterasi berikutnya
