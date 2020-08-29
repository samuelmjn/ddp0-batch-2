# for in string

# String is a collection of characters
# iterasi: mengakses tiap elemen di collection
# String karena bisa diiterasi namanya iterable

for huruf in "abcde":
    print(huruf.upper(), end=" ")  
print()

str_a = "O Semangat"
str_vokal = "aiueoAIUEO"

for huruf in str_a:
    if ((huruf == "e") or (huruf == 'a')):
        print("i", end="")
    else:
        print(huruf, end="")
print()

for huruf in str_a:
    if huruf in str_vokal:  # apakah huruf ada di dalam string str_vokal (substring dari str_vokal)
        print("i", end="")
    else:
        print(huruf, end="")
print()

for _ in str_a:  # kalo variable nya gadipake pake _
    print("aku")


