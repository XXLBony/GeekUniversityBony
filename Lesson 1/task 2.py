timeinsec = int(input('Введите время в секундах: '))
print(str(timeinsec % 3600))
print(str((timeinsec / 60) % 60))
print(str(((timeinsec / 3600) % 60)) % 60)
