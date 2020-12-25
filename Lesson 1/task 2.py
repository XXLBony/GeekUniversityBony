inputstr = input('Введите время в секундах (целое число):')
count = 2
while not inputstr.isdigit() and count:
    count = count - 1
    inputstr = input('Введите время в секундах (целое число):')
if not count:
    print("Необходимо ввсети целое число. Попробуйте в следующий раз.")
    exit(0)
timeinsec = int(inputstr)
print(f'{timeinsec // 3600:02d}:{timeinsec // 60 % 60:02d}:'
      + f'{timeinsec % 60:02d}')
