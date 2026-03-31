from funciones import *
ejercicios = cargar_fichero('ejercicios.json')

salir = False

while salir == False:
    print('\n--- MENÚ EJERCICIOS ---')
    print('1. Listado Ejercicios')
    print('2. Recuento Información')
    print('3. Buscar por condición múltiple')
    print('4. Buscar por músculo principal')
    print('5. Estadística ejercicios')
    print('6. Salir')
    
    opcion = input('Elige una opción: ')
  
    if opcion == '1':
        listar_ejercicios(ejercicios)
    elif opcion == '2':
        recuento_informacion(ejercicios)
    elif opcion == '3':
        busqueda_multiple(ejercicios)
    elif opcion == '4':
        consultar_por_musculo(ejercicios)
    elif opcion == '5':
        ejercicio_libre(ejercicios)
    elif opcion == '6':
        print('Saliendo...')
        salir = True
    else:
        print('Opción no válida, elige entre 1 y 6.')
    