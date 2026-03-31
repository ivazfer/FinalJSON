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

def ejercicio_libre(ejercicios):
    material_buscado = input('Introduce un material: ').lower()
    tipo_buscado = input('Introduce un tipo de ejercicio: ').lower()

    resultados = []

    for ejercicio in ejercicios:
        tipo = ejercicio['clasificacion']['tipo']['nombre'].lower()
        equipo = ejercicio['material']['equipo']

        tiene_material = False

        for elemento in equipo:
            nombre_material = elemento['elemento']['nombre'].lower()
            if nombre_material == material_buscado:
                tiene_material = True

        if tipo == tipo_buscado and tiene_material:
            titulo = ejercicio['nombre']['visible']
            musculo = ejercicio['musculos']['principal']['nombre']
            numero_pasos = len(ejercicio['ejecucion']['pasos'])

            tiene_consejos = 'No'
            if 'consejos' in ejercicio['ejecucion']:
                tiene_consejos = 'Sí'

            resultados.append({
                'titulo': titulo,
                'musculo': musculo,
                'pasos': numero_pasos,
                'consejos': tiene_consejos
            })

    resultados.sort(key=lambda x: x['titulo'])

    print('--- RESULTADOS DEL EJERCICIO LIBRE ---')

    if len(resultados) == 0:
        print('No se han encontrado ejercicios con esas condiciones.')
    else:
        total_pasos = 0

        for ejercicio in resultados:
            print('Título:', ejercicio['titulo'])
            print('Músculo principal:', ejercicio['musculo'])
            print('Número de pasos:', ejercicio['pasos'])
            print('Tiene consejos:', ejercicio['consejos'])
            print('----------------------------------------')

            total_pasos = total_pasos + ejercicio['pasos']

        total_ejercicios = len(resultados)
        media_pasos = total_pasos / total_ejercicios

        print('Total de ejercicios encontrados:', total_ejercicios)
        print('Media de pasos:', round(media_pasos))
    
