# Example 1 (nested branching)

a = 10

if a < 20:
    if a < 5:
        print("ok1")
    elif a > 11:
        print("ok2")
else:
    print("ok3")

# 1 block if
if 0:
    print("1")
elif None:
    print("2")
elif 1:
    print("3")
elif 1:
    print("4")
else:
    print("5")

# Ternary (berguna untuk mengassign value ke variable berdasarkan kondisi tertentu)
# [value_1] if [boolean_expression1] else [value_2] if [boolean_expression2] .... else [value false]

umur = 1
tua = "tua" if umur > 30 else "bayi" if umur < 5 else "muda"

# if umur > 30 :
#     tua = "tua"
print(tua)
