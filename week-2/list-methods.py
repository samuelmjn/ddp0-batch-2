lst = [1, 2, 3]

# append
lst.append('haha')
print(lst)

lst.append([1, 2])
print(lst)
print(len(lst))

# extend
print(lst.extend([1, 2]))
print(lst)

lst.extend([1, 2, [3, 4]])
print(lst)

# majority of list methods returns None

# insert
lst1 = [1, 2, 3]
lst1.insert(5, 'elemen')
print(lst1)

# remove
lst2 = [1, 2, 3, 4, 1]
lst2.remove(1)
print(lst2)

# remove all occurrence
for i in lst2:
    if i == 1:
        lst2.remove(i)

# pop
lst3 = [1, 2, 3]
print(lst3.pop(0))
print(lst3)

# count
murid = ["Dwi", "Nur", "Sri", "Agus", "Indah", "Dwi", "Siti", "Sri", "Nur", "Agus", "Indah", "Agung", "Budi",
         "Hayasaka", "Ade", "Ika", "Dwi"]
print(murid.count("Dwi"))

print(murid.sort(reverse=True))
print(murid)

# reverse
lst4 = [1, 2, 5, 3]
lst4 = lst4[::-1]
print(lst4)

lst4.reverse()  # reverse by index
print(lst4)

# copy (shallow copy)
list1 = [1, 2, 3, [4, 5]]
list2 = list1
list2.append(4)
print(list1, list2)

# shallow copy on multidimensional array
list3 = list1.copy()
list3[3].append(6)
print(list1, list3)

# deepcopy
from copy import deepcopy

list4 = deepcopy(list1)
list4[3].append(6)
print(list1, list4)
print(hex(id(list4[3])), hex(id(list1[3])))

# join, split
ucapan = ['S', 'e', 'l', 'a', 'm', 'a', 't', ' ', 'D', 'a', 't', 'a', 'n', 'g', ' ', 'd', 'i', ' ', 'F', 'a', 's', 'i',
          'l', 'k', 'o', 'm', ' ', 'U', 'I', '!', '!', '!']
a = ",".join(ucapan)

buahbuahan = ["apel", "jeruk", "mangga", "alpukat"]

# print(buahbuahan.split(', '))
# min -> disort ascending, diambil index 0
# max -> disort descending, diambil index 0

print(buahbuahan.sort())
print(sorted(buahbuahan))
print(buahbuahan)

matrix = [[1, 2, 3],  # Ini seperti matriks 3x3
          [4, 5, 6],
          [7, 8, 9]]

print(matrix[0][1])

# list mutability
ab = [1, 2, 3]
ab[0] = 4
print(ab)

# tuple : list tapi tidak mutable
tup = (4, 1, 2, 3)

# ngurutin tipe data iterable dan menghasilkan list itu
sorted_tuple = sorted({1,2,4,0})  # return list
print(tup[1])
print(sorted_tuple)