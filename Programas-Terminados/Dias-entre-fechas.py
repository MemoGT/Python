from datetime import datetime, timedelta

date1 = input("Ingrese la fecha 1 (formato YYYY-MM-DD): ")
date2 = input("Ingrese la fecha 2 (formato YYYY-MM-DD): ")

d1 = datetime.strptime(date1, "%Y-%m-%d")
d2 = datetime.strptime(date2, "%Y-%m-%d")
delta = d2 - d1

print(delta.days)