"""Automated Shopping List"""

NOMBRE_SUPERMERCADO = "Supermercado Fuentes y Familia"
IMPUESTO_DE_VENTAS = 1.13

print ""
print ""
# El nombre del supermercado fue especificado arriba
# para mayor facilidad en caso de querer cambiarlo
print NOMBRE_SUPERMERCADO
print ""

def ajustarimpuesto(precio):
    "Agrega el impuesto de ventas"
    return int(precio) * IMPUESTO_DE_VENTAS

with open('products_list.txt') as products:
    TOTAL = 0
    for line in products:
        # Construye un arreglo de elementos
        # un item por cada columna que se delimita con ,
        # descripcion,precio
        producto = line.split(',')
        precioOriginal = producto[1]
        precioConImpuesto = ajustarimpuesto(precioOriginal)
        print producto[0] + '   ----->  ' + str(precioConImpuesto)
        TOTAL += precioConImpuesto
        if 'str' in line:
            print ""
            break
    print ""
    print 'Total es: ' + str(TOTAL)
    print ""
    # Este es el input de dinero
    DINERO_PAGADO = input('Digite el monto con que desea pagar: ')
    # Tenemos que asegurarnos que el DINERO_PAGADO sea
    # mayor o igual al TOTAL de la factura
    if DINERO_PAGADO >= TOTAL:
        CAMBIO = DINERO_PAGADO - TOTAL
        print 'El vuelto a entregar es: ' + str(CAMBIO)
        print 'Gracias, vuelva pronto!'
    else:
        print 'La cantidad de dinero no alcanza'
        print 'Se necesitan ' + str(TOTAL - DINERO_PAGADO) + ' mas'
        print 'Intente de nuevo'
    print ""
