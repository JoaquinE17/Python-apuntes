COMO SABER CUANDO USAR CADA UNA
===============================

Elegir entre **listas**, **tuplas**, **sets** y **diccionarios** en Python depende del tipo de operación que quieras realizar y las características específicas de cada estructura de datos. Aquí te explico cuándo usar cada una de ellas:

### 1. **Listas (`list`)**:
- **Cuándo usar**: Si necesitas una **colección ordenada** y **modificable** (es decir, que puedes agregar, eliminar o modificar elementos). Las listas son muy útiles cuando el orden de los elementos importa y puedes necesitar realizar cambios o accesos por índice.
- **Características**:
  - **Ordenadas** (los elementos mantienen el orden en el que se agregan).
  - **Mutables** (puedes cambiar, agregar y eliminar elementos).
  - Pueden contener **duplicados**.
  - Se accede a los elementos por índice.
  
- **Ejemplo de uso**:
  ```python
  lista = [1, 2, 3]
  lista.append(4)  # Añadir un elemento
  lista[0] = 10    # Modificar un elemento
  ```

### 2. **Tuplas (`tuple`)**:
- **Cuándo usar**: Si necesitas una **colección ordenada** pero **inmutable** (no se pueden cambiar, agregar ni eliminar elementos después de su creación). Son ideales para almacenar datos que no deben modificarse, como coordenadas o configuraciones fijas.
- **Características**:
  - **Ordenadas**.
  - **Inmutables** (no puedes modificar, agregar ni eliminar elementos una vez creada).
  - Pueden contener **duplicados**.
  - Se accede a los elementos por índice.

- **Ejemplo de uso**:
  ```python
  tupla = (1, 2, 3)
  # tupla[0] = 10  # Esto dará error, porque las tuplas son inmutables
  ```

### 3. **Sets (`set`)**:
- **Cuándo usar**: Si necesitas una **colección no ordenada** y **sin elementos duplicados**. Los sets son ideales cuando solo te interesa la existencia de elementos, sin importar su orden o si se repiten.
- **Características**:
  - **No ordenados** (no se puede acceder a los elementos por índice).
  - **No permiten duplicados** (cada elemento aparece una sola vez).
  - **Mutables** (puedes agregar o eliminar elementos).
  - Son útiles para operaciones de conjuntos como unión, intersección y diferencia.
  
- **Ejemplo de uso**:
  ```python
  set1 = {1, 2, 3}
  set1.add(4)  # Añadir un elemento
  set1.remove(1)  # Eliminar un elemento
  ```

### 4. **Diccionarios (`dict`)**:
- **Cuándo usar**: Si necesitas una **colección de pares clave-valor**, donde puedes acceder rápidamente a un valor mediante una **clave única**. Los diccionarios son ideales cuando necesitas asociar información, como un registro de usuarios o configuraciones por nombre.
- **Características**:
  - **No ordenados** en versiones anteriores a Python 3.7 (en Python 3.7+ mantienen el orden de inserción).
  - Las claves deben ser **únicas** y **inmutables**.
  - Los valores pueden ser de cualquier tipo y ser **mutables**.
  - **Acceso rápido** a los elementos mediante claves.

- **Ejemplo de uso**:
  ```python
  diccionario = {'nombre': 'Juan', 'edad': 30}
  diccionario['edad'] = 31  # Modificar un valor
  diccionario['direccion'] = 'Calle Falsa 123'  # Añadir un nuevo par clave-valor
  ```

### Resumen de cuándo usar cada estructura:

- **Lista**: Cuando necesitas **orden** y la capacidad de **modificar** los elementos.
- **Tupla**: Cuando necesitas **orden** pero no necesitas modificar los elementos.
- **Set**: Cuando necesitas una **colección sin duplicados** y no te importa el orden.
- **Diccionario**: Cuando necesitas almacenar **pares clave-valor** y acceder a los valores rápidamente mediante una clave.

### Consejos adicionales:
- Si no necesitas **duplicados**, el **set** puede ser más eficiente.
- Si te importa **el orden de los elementos** y quieres poder **modificarlos**, usa una **lista**.
- Si necesitas un **mapeo rápido** de claves a valores (como una base de datos simple), el **diccionario** es la mejor opción.
- Si los datos no deben cambiar, usa una **tupla** para garantizar su inmutabilidad.

Cada estructura tiene sus fortalezas dependiendo del uso que le quieras dar.