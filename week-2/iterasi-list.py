lst =  [2006, 3.14, 'Hello, World!', False, [7, 8, 9]]  # panjang = 5

# Untuk mencetak semua objek pada list, dapat menggunakan looping
for i in range(len(lst)):  # iterasi index nya, len() -> panjang list
	print(lst[i], end=' ')

print()

# atau bisa dengan
for i in lst:
	print(i, end=' ')

# Kedua output sama yaitu:
# 2006 3.14 'Hello, World!' False [7, 8, 9]
