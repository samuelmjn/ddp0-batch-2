string_a = "Halo Kamu"

# indexing (mengakses karakter pada index tertentu)

print(string_a[3])
print(string_a[-6])

# slicing (memotong bagian dari string itu)
# [start:finish:steps]
# default [0:panjang_string:1]

print(string_a[5:8]) #Kam
print(string_a[5:]) #Kamu

print(string_a[::2])

# special case
# kalo steps negatif dia akan mulai dari belakang
# default [panjang_String:0:(negatif)]

# ngebalik string
print(string_a[::-1])

print(string_a[:4:-1]) # sama
print(string_a[:-5:-1]) # sama

# Error index out of range
# indexing di luar index yang ada

str_b = "anak"
# print(str_b[4])

# gak berlaku di slicing
print(str_b[:9])

slicing_0 = str_b[0:0]
print(len(slicing_0))

