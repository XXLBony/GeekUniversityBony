inputstr = input('Введите число от 0 до 9:')
count = 2
while not inputstr.isdigit() and count:
    count = count - 1
    inputstr = input('Введите число от 0 до 9:')
if not count:
    print("Необходимо ввести число от 0 до 9: Попробуйте в следующий раз.")
    exit(0)
