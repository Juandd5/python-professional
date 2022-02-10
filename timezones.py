from datetime import datetime
import pytz

#en una variable guardo el timezone, le paso como parámetro
#el timezone de mexico que se puede ver en la base de datos
bogota_timezone = pytz.timezone('America/Bogota')
#now() puede recibir un objeto de tipo pytz para trabajar con los timezones
# si no le paso ningún parámetro, trae la hora de mi pc o la hora universal
colombia_date = datetime.now(bogota_timezone)
print('Colombia: ', colombia_date.strftime('%d/%m/%Y, %I:%M %p'))

mexico_timezone = pytz.timezone('America/Mexico_City')
mexico_date = datetime.now(mexico_timezone)
print('Ciudad de México:', mexico_date.strftime('%d/%m/%Y, %I:%M:%S %p'))

argentina_timezone = pytz.timezone('America/Argentina/Buenos_Aires')
argentina_date = datetime.now(argentina_timezone)
print('Argentina: ', argentina_date.strftime('%d/%m/%Y, %H:%M:%S'))

usa_timezone = pytz.timezone('America/New_York')
usa_date = datetime.now(usa_timezone)
print('Estados Unidos: ', usa_date.strftime('%m/%d/%Y, %H:%M:%S'))

london_timezone = pytz.timezone('Europe/London')
london_date = datetime.now(london_timezone)
print('Londres : ', london_date.strftime('%m/%d/%Y, %H:%M:%S'))