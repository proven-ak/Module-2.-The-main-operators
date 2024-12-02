first_num = int(input("Введите число от 3 до 20 : "))

result = ""
pass_list = []

for i in range(1, 20):
    for j in range(i, 20):
        if i != j:
            if first_num % (i + j) == 0:
                str_ = str(i) + str(j)
                pass_list.append(str_)
                result = "".join(pass_list)

print(result)

