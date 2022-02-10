from datetime import datetime, date

my_time = datetime.now() #fecha y hora actual
print(my_time)

my_time = datetime.utcnow() #hora universal
print(my_time)

my_date = date.today()
print(my_date)
print(f'Year: {my_date.year}')
print(f'Month: {my_date.month}')
print(f'Day: {my_date.day}')

my_datetime = datetime.now()
print(my_datetime)

my_str = my_datetime.strftime('%d/%m/%Y')
print(f'Formato LATAM: {my_str}')

my_str = my_datetime.strftime('%m/%d/%Y')
print(f'Formato USA: {my_str}')

my_str = my_datetime.strftime('Estamos en el año %Y')
print(f'Formato random: {my_str}')

my_str = my_datetime.strftime('%H:%M')
print(f'La hora es: {my_str}')

my_str = my_datetime.strftime('%I:%M %p')
print(f'La hora es: {my_str}')
