# Grupo 7 — Funciones, parámetros y docstrings

## Integrantes y Tema
* **Integrantes:** Ignacio Ibáñez-Rizo, Pablo Legorburo y Jorge Durá
* **Tema:** Funciones en Python, parámetros, argumentos, valores por defecto, instrucción `return`, docstrings y comentarios.

---

## Qué demuestra el ejemplo y cómo ejecutarlo
* **Qué demuestra:** Este ejemplo ilustra la definición de funciones en Python, el uso de parámetros obligatorios y opcionales (con valores por defecto), la documentación formal mediante *docstrings* y el uso de la instrucción `return` para devolver resultados.
* **Cómo ejecutarlo:** 
  1. Guarda el código en un archivo llamado `ejemplo.py`.
  2. Abre la terminal en el directorio del archivo y ejecuta:
     ```bash
     python ejemplo.py
     ```

---

## Resultado esperado
Al ejecutar el script, se mostrará en la consola el resultado de ambas llamadas:
```text
30
10
```

---

## Pregunta para la clase y su respuesta

* **Pregunta:** ¿Qué ocurre si llamamos a la función sin proporcionar ningún argumento (ej. `calcular_precio()` )?
* **Respuesta:** Se genera un error de tipo `TypeError` porque el parámetro `precio` es obligatorio al no tener definido ningún valor por defecto.

---

## Error típico o modificación explicada

* **Error típico:** Olvidar la instrucción `return` al final de la función. Si se omite, la operación interna se realiza pero la función devuelve `None` implícitamente, haciendo que los `print` muestren `None` en lugar de los valores calculados.