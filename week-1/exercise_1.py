# Link Soal
# Bagian The Key Value Method
# http://mathforum.org/dr.math/faq/faq.calendar.html

# minta tanggal dari pengguna
user_input = input("Masukkan tanggal dalam format DD-MM-YYYY: ")

# misahin tanggal bulan tahun
date = int(user_input[:2])
month = int(user_input[3:5])
year = int(user_input[6:])

# operasi
hasil = year % 100  # dapet 2 angka terakhir tahun
hasil //= 4
hasil += date

# ditambah sesuai table month's key value
if month == 1 or month == 10:
    hasil += 1
elif month == 2 or month == 3 or month == 11:
    hasil += 4
elif month == 4 or month == 7:
    hasil += 0
elif month == 5:
    hasil += 2
elif month == 6:
    hasil += 5
elif month == 8:
    hasil += 3
elif month == 9:
    hasil += 6

# cek apakah januari atau february di tahun kabisat
# | or, & and, ~ not
if (month == 1 | month == 2) & (year % 4 == 0 & year % 100 != 0 | year % 400 == 0):
    hasil -= 1

# ditambah sama table century code
if year // 100 == 17:
    hasil += 4
elif year // 100 == 18:
    hasil += 2
elif year // 100 == 19:
    hasil += 0
elif year // 100 == 20:
    hasil += 6

# ditambah sama 2 angka terakhir di tahun
hasil += year % 100

# nentuin hari
if hasil % 7 == 1:
    print('Sunday')
elif hasil % 7 == 2:
    print('Monday')
elif hasil % 7 == 3:
    print('Tuesday')
elif hasil % 7 == 4:
    print('Wednesday')
elif hasil % 7 == 5:
    print('Thursday')
elif hasil % 7 == 6:
    print('Friday')
elif hasil % 7 == 0:
    print('Saturday')
