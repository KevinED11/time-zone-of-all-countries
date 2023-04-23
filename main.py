import pytz
import datetime

TIME_ZONES = pytz.all_timezones

for time_zone in TIME_ZONES:
    print(time_zone)


time = pytz.timezone('America/Mexico_City').localize(datetime.datetime.now())
ZONE = pytz.timezone('America/Mexico_City')
ZONE2 = pytz.timezone('America/Mazatlan')


NOW = datetime.datetime.now(ZONE)
NOW2 = datetime.datetime.now(ZONE2)
print(f"THE TIME IS: {time}")
print(NOW)
print("Hora actual en Ciudad de México:", NOW.strftime("%H:%M:%S"))
print("Hora actual en Ciudad de mazatlan es:", NOW2.strftime("%H:%M:%S"))
country_time_zones = pytz.country_timezones("MX")
countryz = pytz.country_names
print("ZONAS HORARRIAS DEL PAIS ABAJO")
print(country_time_zones)
mx = dict(countryz)
print(f"\n {dict(countryz)}")
# time = pytz.timezone("America/Mexico_City")
filter_mx = [(key, value) for key, value in mx.items() if key == "BV"]
print(filter_mx)

zonas_horarias_mexico = {}
for country_zone in country_time_zones:
    print(country_zone)
    zonas_horarias_mexico[country_zone] = datetime.datetime.now(
        pytz.timezone(country_zone)).strftime("%H:%M:%S")

horarios = {zone_name: datetime.datetime.now(
    pytz.timezone(zone_name)).strftime("%H:%M:%S") for zone_name in country_time_zones}
print(zonas_horarias_mexico)
print("\n")
print(horarios)

all_zones = dict(pytz.country_names)
print("\ntodos los paises abajo")
print(all_zones)

all_zones.pop("BV")
all_zones.pop("HM")
all = {}
for zone, name_pais in all_zones.items():
    
    timezone = pytz.country_timezones(zone)
    all[name_pais] = {"Zonas horarias": timezone, "hora por zona horaria": {zona: datetime.datetime.now(pytz.timezone(zona)).strftime("%H:%M:%S") for zona in timezone}} 
print("\nCADA PAIS CON SUS RESPECTIVAS ZONAS HORARIAS")
print(all)

print("\nZONAD HORARIAS DEL PAIS DE MÉXICO")
print(all["Mexico"])
