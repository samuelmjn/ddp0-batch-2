# Deklarasi/membuat list kosong, dapat dengan cara
lst = list()

# atau dengan cara
lst = []

print(lst)

# Bisa juga kita deklarasikan dengan elemennya
lst = [2006, 3.14, "Hello, World!", False, [7, 8, 9]]

print(lst)

# Selain itu, kita dapat membuat sebuah list dari String
lst = list("Hello") # Akan menghasilkan ['H', 'e', 'l', 'l', 'o']

print(lst)

## Mengakses / indexing

# Misal kita gunakan list sebelumnya
lst = [2006, 3.14, "Hello, World!", False, [7, 8, 9]]

# Bagaimana cara kita mencetak "Hello, World!" pada list kita?
print(lst[2])    # Output: 'Hello, World!'

# Bagaimana dengan angka 8 dalam list?
print(lst[4][1])    # Output: 8

## Slicing

# Misal diberikan list sebagai berikut:
lst1 = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")  # ubah String -> list dari karakter2nya
print('lst1 : ', lst1)
# Dari list tersebut ingin diambil 5 huruf pertama, maka:
lst2 = lst1[:5]    # lst2 = ['A', 'B', 'C', 'D', 'E']
print(lst2)

# Beberapa mungkin berpikir untuk memulai dari 21 hingga akhir seperti ini
lst3 = lst1[21:]    # ['V', 'W', 'X', 'Y', 'Z']

# Tetapi, bagaimana jika kita tidak mengetahui panjang list tersebut? Kita dapat menggunakan index negatif, seperti ini:

lst3 = lst1[-5:]    # ['V', 'W', 'X', 'Y', 'Z']
print(lst3)