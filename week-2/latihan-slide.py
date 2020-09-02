# latihan 1

print(["Semangat"] + 2 * ["Ka"] + ["k!"])  # ['Semangat', 'Ka', 'Ka', 'k!']
print(list("CSUI2020"))  # ['C', 'S', 'U', 'I', '2', '0', '2', '0']
print(5 * list(range(1, 2)))  # range(1, 2), 2 -> eksklusif alias gaikut
# [1, 1, 1, 1, 1]

# latihan 2

lst = [2]

if len(lst) == 0:
	print(True)
else:
	x = lst[0]
	for i in lst:
		if x != i:
			print(False)
			break
	else:		
		print(True)

# mengecek apakah elemen elemen dalam list tersebut seragam atau tidak. 