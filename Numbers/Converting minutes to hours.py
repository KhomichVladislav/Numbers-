minutes = int(input("Введите количество минут"))
hours = minutes // 60
remaining = minutes % 60
print(hours, "часов", remaining, "минут")