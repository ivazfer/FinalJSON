https://github.com/everkinetic/data/blob/main/exercises.json

Cambios realizados

Se ha reestructurado el archivo JSON original para hacerlo más claro, completo y organizado. Ahora parte de una lista principal de ejercicios, donde cada uno es un objeto independiente con bloques internos como nombre, descripción, clasificación, músculos, material y ejecución.

Además, se han traducido los campos al español para mantener uniformidad, se han eliminado datos innecesarios y se ha aumentado la complejidad mediante una estructura jerárquica con varios niveles, sustituyendo datos simples por objetos y subobjetos relacionados.

Estructura del JSON

id: identificador único del ejercicio.
nombre: objeto con el identificador interno y el nombre visible.
descripcion: objeto con un resumen descriptivo.
clasificacion: objeto que indica el tipo de ejercicio.
musculos: objeto con el músculo principal y los secundarios.
material: objeto con el equipamiento necesario.
ejecucion: objeto con los pasos de realización y, a veces, consejos extra.

Ejercicios

1- Listado de información
Mostrar el título visible de todos los ejercicios, así como el tipo de ejercicio y el músculo principal asociado a cada uno de ellos.

2- Recuento de información
Mostrar cada ejercicio junto con el número de pasos necesarios para su ejecución. Al final del listado, indicar el número total de ejercicios en el archivo JSON.

3- Búsqueda con condición múltiple
Solicitar por teclado un tipo de ejercicio y un músculo principal, y mostrar únicamente aquellos ejercicios que coincidan simultáneamente con ambos criterios.

4- Consulta de información relacionada
Solicitar por teclado el nombre de un músculo principal y mostrar los ejercicios vinculados a dicho músculo junto con el material requerido para su realización.

5- Ejercicio libre con ordenación y estadística
Solicitar por teclado un material de entrenamiento y un tipo de ejercicio. A continuación, mostrar los ejercicios que cumplan ambas condiciones, ordenados alfabéticamente por título, indicando para cada uno el músculo principal, el número de pasos y si dispone o no de consejos. Finalmente, mostrar una estadística con el total de ejercicios encontrados y la media de pasos correspondiente.


