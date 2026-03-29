from funciones import *
ejercicios = cargar_fichero('ejercicios.json')

salir = False

while salir == False:
    print('\n--- MENÚ EJERCICIOS ---')
    print('1. Listado Ejercicios')
    print('2. Recuento Información')
    print('6. Salir')
    
    opcion = input('Elige una opción: ')
  
    if opcion == '1':
        listar_ejercicios(ejercicios)
    elif opcion == '2':
        recuento_informacion(ejercicios)
    elif opcion == '6':
        print('Saliendo...')
        salir = True
    else:
        print('Opción no válida, elige entre 1 y 6.')
    