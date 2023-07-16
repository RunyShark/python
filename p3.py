trabajador = input('nombre del colaborador: ')
venta = input('monto total de venta: ')
venta = float(venta)
venta = round(venta)

print(f'Hola! {trabajador} tu comicion es: {round(venta * 0.13, 2)}')
