date = input('Masukan tanggal')
day = date[:2]
month = date[3:5]
year = date[6:]

temp = int(year[2:])
temp //= 4
temp += int(day)

if month == '01':
    temp += 1
elif month == '02':
    temp += 4
elif month == '03':
    temp += 4
elif month == '04':
    temp += 0
elif month == '05':
    temp += 2
elif month == '06':
    temp += 5
elif month == '07':
    temp += 0
elif month == '08':
    temp += 3
elif month == '09':
    temp += 6
elif month == '10':
    temp += 1
elif month == '11':
    temp += 4
elif month == '12':
    temp += 6

if ((int(year) % 4 == 0 and int(year) % 100 != 0) or int(year) % 400 == 0) and (month == '01' or month == '02'):
    temp -= 1

century = int(year[:2])
# handle abad jika lebih dari abad 2000s
if century > 20:
    while century > 20:
        century -= 4

if century < 17:
    while century < 17:
        century += 4

if century == 17:
    temp += 4
elif century == 18:
    temp += 2
elif century == 19:
    temp += 0
elif century == 20:
    temp += 6

temp += int(year[2:])

res = temp % 7
if res == 1:
    print('Sunday')
elif res == 2:
    print('Monday')
elif res == 3:
    print('Tuesday')
elif res == 4:
    print('Wednesday')
elif res == 5:
    print('Thursday')
elif res == 6:
    print('Friday')
elif res == 0:
    print('Saturday')
