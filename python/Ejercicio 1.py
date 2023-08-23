"""meses1 = list(['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio'])
meses2 = list(['julio', 'agosto', 'septiembre', 'octubre'])
meses3 = list(['noviembre', 'diciembre'])
sueldo = list([300, 500, 700])"""
i=0
promedio = 0
meses = ['enero ', 'febrero ', 'marzo ', 'abril ', 'mayo ', 'junio ','julio ', 'agosto ', 'septiembre ', 'octubre ','noviembre ', 'diciembre ']
sueldo = [300,300,300,300,300,300,500,500,500,500,700,700]

while i < 12:
    print(meses[i] + str(sueldo[i]))
    promedio = promedio + sueldo[i]
    i=i + 1

    promedio= promedio / 12
    print(int(promedio))

if sueldo < 300:
    print("el sueldo es bajo")
else: sueldo 
