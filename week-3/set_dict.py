# Set (Himpunan) = {1,2,3,4}
# mutable : bisa dimutate/ dimodif/ diubah isinya
# tidak terurut (not subscriptable)
# tiap elemennya dianggap unik

# deklarasi
himpunan_a = set()
print(himpunan_a)
himpunan_b = {'a', 'b', 'e', 'd', 'a'}
print(himpunan_b)  # cuma ambil yg unik
print(len(himpunan_b))

# himpunan_c = list('abc')
himpunan_c = set('abc')
print(himpunan_c)

# iterasi set
set_a = {'a', 'b', 'c'}
for elemen in set_a:
    print(elemen)

# basic method
# add() : nambah
set_a = {'a', 'b', 'c'}
set_a.add('d')
print(set_a)
set_a.remove('a')
print(set_a)

# operasi himpunan
# Intersection (irisan)
set_a = {'a', 'b', 'c'}
set_b = {'c', 'd', 'e'}

print(set_a.intersection(set_b))
print(set_a & set_b)

# Union (gabungan)
print(set_a.union(set_b))
print(set_a | set_b)

# Difference (kurang)
print(set_a.difference(set_b))
print(set_a - set_b)

# Symmetric Difference (XOR)
print(set_a.symmetric_difference(set_b))
print(set_a ^ set_b)

# Subset (himpunan bagian) / Superset (himpunan kuasa)
set_b = {'a', 'b', 'c', 'd'}
set_a = {'a', 'b', 'c'}
print(set_a.issubset(set_b))
print(set_a <= set_b)

print(set_b.issuperset(set_a))
print(set_b >= set_a)


# dictionary = { 'nama' : 'gani', 'umur' : 19 }
# mutable (valuenya bisa diganti)
# key: integer, string, boolean, tuple (unik dan gabisa diubah[imutable])
# valuenya: bebas

# deklarasi
dict_a = {}
dict_b = {
    'nama': 'Gani',
    'umur': 19,
    1: 'ko',
    True: 9009,
    'alamat': {
        'desa': 'Mambak',
        'kecamatan': 'Pakis Aji',
        'kota': 'Jepara'
    },
    (1,2): 'a tuple key',
}

print(dict_b['umur'])
print(dict_b[True])
print(dict_b['alamat']['kota'])
# print(dict_b['tinggi'])  # keyerror

# cara nambahin key value baru
dict_b['universitas'] = 'UI'
print(dict_b)

# cara ngubah 1 value
dict_b['universitas'] = 'Nanyang'
print(dict_b)

# cara ngubah banyak value
dict_b.update({'umur': 9, 'nama': 'ilham'})
print(dict_b)

# copy
dict_c = dict_b.copy()
print(dict_c)

# hapus
dict_c.pop((1,2))  # key yg mau dihapus
print(dict_c)

# cek apakah suatu key ada di dict
print('hobi' in dict_b)

# iterasi
# secara default dia bakal iterasi key nya

for k in dict_b:
    print(k)

# sama kaya
for k in dict_b.keys():
    print(k)

# iterasi value
for v in dict_b.values():
    print(v)

# iterasi dua2nya (key sama value)
for k,v in dict_b.items():
    print(str(k) + ':' + str(v))

# panjang
print(len(dict_b))

# ngosongin dict
dict_b.clear()
print(dict_b)