# latihan 1
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 1 2 3
# 4 5 6
# 7 8 9
#
# 1 4 7
# 2 5 8
# 3 6 9


# Wafi
# a = [[1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]]

# x = len(a)
# y = len(a[0])

# ta =  []

# for n in range(0, y):
#     for i in range(0, x):
#         ta.append(a[i+n][i])

# print(ta)

matrix = [
[1, 2, 3, 5], 
[4, 5, 6, 5], 
[7, 8, 9, 5]
]

# bikin 2 variable
matrix2 = []  # hasil akhirnya
# jadi penampung baris sementara
temp = []

for i in range(len(matrix[0])):
    for j in range(len(matrix)):
        temp.append(matrix[j][i])
    else:
        matrix2.append(temp)
        print(temp)
        temp = []

print(matrix2)
