opcion = 100
while opcion != 0:
    print("****** Las etapas de la vida ******")
    print("1. Determinar tu etapa de vida")
    print("0. Salir")
    opcion = int(input("Digita una opción: "))
    
    if opcion == 1:
        currentDay=23
        currentMonth=8
        currentYear=2023
        # b = birthday
        bDay= int(input('Ingrese su dia de Cumpleaños: '))
        bMonth = int(input('Ingrese su mes de Cumpleaños: '))
        bYear = int(input('Ingrese su año de Cumpleaños: '))
        age = currentYear - bYear
        if age >= 15 and currentMonth >= bMonth:
            if currentDay > bDay:
                age += 1
        if age >= 0 and age <= 14:
            print('Categoria niño')
        elif age >= 15 and age <= 28:
            print("Categoria Joven")
        elif age >= 28 and age <= 60:
            print("Categoria Adulto")
        elif age >= 60:
            print("Categoria Adulto Mayor")
    elif opcion == 0:
        print("Gracias, hasta pronto.")
    else:
        print("Opción inválida.")