# Wafi
n = int(input("Piramida berapakah yang anda inginkan? "))

for i in range(1,n+1):
    print("*" * (i))

# Aiko
ukuran_piramida = input('Masukkan ukuran piramida yang kamu mau: ')

if int(ukuran_piramida) > 0:
    for i in range (1, int(ukuran_piramida) + 1):
        print('*' * i)

# Helga
num = int(input("ukuran piramida: "))

for i in range(1,num):
    print("*" * i)
else:
    while (num!=0):
        print("*" * num) 
        num -= 1 