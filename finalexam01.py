m = float(0)
print('i', 'm(i)')
for i in range(1, 902):
    a = (-1) ** (i + 1)
    b = (2 * i) - 1
    m += a / b
    if i == 1 or i > 100:
        print(i, format(round(m * 4, 4), '.4f'))
