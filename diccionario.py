productoTerminadoUno={
    'referencia':5087, 
    'marca':"Americanino",
    'descripcion':"Chompa de acampar",
    'color':"Naranja",
    'costoUnitario':100000,
    'dipodibleBodega':True,
    'constoVenta':850000,
    'puntosVenta':['CC Mayorca', 'Terminal Norte', 'Puerta Del Norte', 'Centro De La Moda']
}
productoTerminadoDos={
    'referencia':5088, 
    'marca':"Americanino",
    'descripcion':"Camiseta Polo",
    'color':"Azul Oscuro",
    'costoUnitario':30000,
    'dipodibleBodega':True,
    'constoVenta':150000,
    'puntosVenta':['CC Mayorca', 'Terminal Norte', 'Puerta Del Norte', 'Centro De La Moda']
}

#Creando una lista de diccionarios
productos=[productoTerminadoUno, productoTerminadoDos]

#Recorriendo una lista con ciclo FOR
'''for contador in range(1, 10,2):
    print(contador)'''

for producto in productos:
    for puntoVenta in producto["puntosVenta"]:
        print(puntoVenta)