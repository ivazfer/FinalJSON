import json
def cargar_fichero(ruta="ejercicios.json"):
    with open(ruta, encoding="utf-8") as f:
        datos = json.load(f)
    return datos["ejercicios"]

def listar_ejercicios(ejercicios):
        for ejercicio in ejercicios:
            titulo = ejercicio["nombre"]["visible"]
            tipo = ejercicio["clasificacion"]["tipo"]["nombre"]
            musculo = ejercicio["musculos"]["principal"]["nombre"]
            
            print("Titulo: ", titulo)
            print("Tipo: ", tipo)
            print("Musculo Principal", musculo)
            print("------------------")
            print()
            
            