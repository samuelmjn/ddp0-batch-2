# angka = int(input('Masukkan angka: '))

dict_a = {'nama': 'gani'}
list_a = [1,2]

try:
    print(dict_a['umur'])
    print(list_a[100])
except KeyError:
    umur = int(input('umur gaada, masukkan umur : '))
    dict_a['umur'] = umur
    print(dict_a['umur'])
except IndexError:
    print('kelebihan indexnya')

# meskipun ada banyak except dia cuman masuk ke salah satunya yang ditemuin pertama

print('selese')