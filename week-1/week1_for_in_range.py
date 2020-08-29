# for in range

# for <VAR> in range(start, stop, step):
# 		<LOOP BODY>

# range(stop)
# range(start,stop)
# range(start,stop,step)

for i in range(11,0,-1): # sama halnya dengan range(0,11,1)
    # if i % 2 == 0:
    #     print("genap")
    # else:
    print(i)

# print(*values, end, sep)
print("-"*50)

for i in range(6):
    print(i, end=" ")  # end: karakter yang ditambahkan setelah semua value di print(*values) tercetak
print()  # print string '' dengan end="\n"
print("halo")

print("-"*50)
print(1,2,3,4, sep="+")  # sep: sebagai pemisah antar value di print(value1,value2,...)
print()

# len() : fungsi untuk me-return integer panjang suatu collections/ iterable, salah satunya string
for i in range(len("kamu")):
    print(i)
