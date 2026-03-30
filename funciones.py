import json
def cargar_fichero(ruta='ejercicios.json'):
    with open(ruta, encoding='utf-8') as f:
        datos = json.load(f)
    return datos['ejercicios']

def listar_ejercicios(ejercicios):
        for ejercicio in ejercicios:
            titulo = ejercicio['nombre']['visible']
            tipo = ejercicio['clasificacion']['tipo']['nombre']
            musculo = ejercicio['musculos']['principal']['nombre']
            
            print('Título: ', titulo)
            print('Tipo: ', tipo)
            print('Musculo Principal', musculo)
            print('------------------')
            print()

def recuento_informacion(ejercicios):
    total_ejercicios = len(ejercicios)

    print("--- RESULTADOS---")
    for ejercicio in ejercicios:
        titulo = ejercicio['nombre']['visible']
        total_pasos = len(ejercicio['ejecucion']['pasos'])
        
        print('Título: ', titulo)
        print('Número de pasos: ',total_pasos)
        print('------------------')
        print()
        
    print('Hay un total de ', total_ejercicios, ' ejercicios.')

def busqueda_multiple(ejercicios):
    tipo_buscado = input('Introduce el tipo de ejercicio: ').lower()
    musculo_buscado = input('Introduce el músculo principal: ').lower()

    print('--- RESULTADOS DE LA BÚSQUEDA ---')
    encontrado = False 
    for ejercicio in ejercicios:
        tipo = ejercicio['clasificacion']['tipo']['nombre'].lower()
        musculo = ejercicio['musculos']['principal']['nombre'].lower()

        if tipo == tipo_buscado and musculo == musculo_buscado:
            titulo = ejercicio['nombre']['visible']
            print('Título:', titulo)
            print('Tipo:', ejercicio['clasificacion']['tipo']['nombre'])
            print('Músculo principal:', ejercicio['musculos']['principal']['nombre'])
            print('------------------')
            print()
            encontrado = True  

    if encontrado == False:
        print('No hay coincidencias')

def consultar_por_musculo(ejercicios):
    musculo_buscado = input('Introduce el músculo principal: ').lower()
    encontrado = False

    print('--- EJERCICIOS RELACIONADOS ---')
    for ejercicio in ejercicios:
        musculo = ejercicio['musculos']['principal']['nombre'].lower()

        if musculo == musculo_buscado:
            titulo = ejercicio['nombre']['visible']
            equipo = ejercicio['material']['equipo']

            print('Título:', titulo)
            print('Material necesario:')

            for elemento in equipo:
                nombre_material = elemento['elemento']['nombre']
                tipo_material = elemento['elemento']['tipo']
                print('- ', nombre_material,'(',tipo_material,')')
            encontrado = True

    if encontrado == False:
        print('No se han encontrado ejercicios para ese músculo principal.')

    
