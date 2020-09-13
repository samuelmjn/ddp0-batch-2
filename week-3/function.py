# luas(panjang, lebar) -> panjang * lebar

# contoh fungsi yang tidak mereturn apapun
def luas(panjang, lebar):
    print(panjang * lebar)

print(luas(5,9)) # langkahnya, print di dalam body luas() dijalankan namun luas() ga return apa2

# contoh fungsi yang memiliki return
def luas(panjang, lebar):
    return (panjang * lebar)

print(luas(3,3))  # yang terjadi print(70)

# len() itu juga sebuah function
# method vs function
# method itu adalah function yang melekat pada suatu tipe data/ object tertentu

set_a = {1,2}
set_a.add(3)
# add() itu method

# deklarasi function
# def <nama_function>():
# 	<body>

def ucapan():
    print('selamat pagi')


# calling a function
ucapan()

# pengisian parameter
# berdasarkan urutan
print(luas(2,3))
#berdasarkan parameternya
print(luas(lebar=10, panjang=3))

def volume(panjang, lebar, tinggi):
    return luas(panjang, lebar) * tinggi

print(volume(3,3,3))

# def main():
#     tanya_input()
#     hitung()
#     print_sesuatu()

# main()