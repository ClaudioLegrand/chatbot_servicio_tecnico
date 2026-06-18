# 🤖 Chatbot de Servicio Técnico - Presupuestos Automatizados

Proyecto integrador para la automatización del proceso de Soporte Técnico (Nivel 1), desarrollado en Python. Este sistema simula la atención automatizada a clientes mediante una interfaz de línea de comandos (CLI), gestionando garantías, inventario de repuestos, asignación de turnos y derivaciones a técnicos.

**Autores:** Claudio Legrand y Mariano Gallo  
**Institución:** Universidad Tecnológica Nacional (UTN) - Facultad Regional San Nicolás  

---

## ⚙️ Arquitectura del Proyecto

El código aplica el paradigma "Top-Down" y está modularizado para separar las responsabilidades del sistema:

* `main.py`: Orquestador principal del flujo del programa.
* `telegram.py`: Simulación de la vista (interacción con el usuario, menús y validación de entradas).
* `logica_bot.py`: Controlador que maneja el árbol de decisiones del negocio (BPMN).
* `base_datos.py`: Gestión de persistencia de datos (lectura y escritura de archivos).
* `turnos.py`: Motor lógico para calcular fechas hábiles y asignar disponibilidad.

---

## 🚀 Requisitos y Despliegue

El proyecto fue diseñado para ser liviano y no requiere la instalación de librerías externas mediante `pip`. Utiliza exclusivamente módulos nativos de Python (`os`, `csv`, `datetime`).

### Pasos para ejecutar el proyecto:

1.  **Clonar o descargar el repositorio:** Asegúrate de que todos los archivos `.py` estén dentro de la misma carpeta.
2.  **Verificar la versión de Python:** Se requiere Python 3.x instalado en el sistema.
3.  **Ejecución:** Abre una terminal, navega hasta la carpeta del proyecto y ejecuta el archivo principal:
    ```bash
    python main.py
    ```
4.  **Generación de Datos:** Al ejecutarse por primera vez, el sistema detectará automáticamente la ausencia de bases de datos y creará los archivos `.csv` necesarios (`clientes.csv`, `stock_repuestos.csv`, `garantias.csv`, `tickets.csv`) y la bandeja del técnico (`bandeja_tecnico.txt`) con datos "Mock" (de prueba) para simular el entorno.

> **Nota para Pruebas:** Si deseas reiniciar la base de datos a su estado original (fábrica), simplemente elimina los archivos `.csv` y `.txt` generados en la carpeta. El sistema los volverá a crear en la próxima ejecución.

---

## 📖 Manual de Usuario (Guía Rápida)

El flujo de interacción con el chatbot sigue estos pasos estandarizados:

1.  **Identificación:** Al ejecutar el sistema, el bot solicita el ingreso del DNI. Se deben ingresar **solo valores numéricos sin puntos ni espacios**. El sistema forzará un bucle de validación si se ingresan letras.
2.  **Registro:** Si el DNI no figura en la base de datos, se solicitará el nombre (solo letras) para dar de alta al nuevo cliente.
3.  **Máquina de Estados y Garantías:** El bot verificará internamente si el cliente tiene trámites previos pendientes o si su equipo se encuentra bajo garantía. En caso afirmativo, informará el estado actual e interrumpirá el flujo de presupuestación.
4.  **Menú de Diagnóstico:** De no poseer garantía ni trámites previos, el bot desplegará un menú de opciones (1 al 7) con las fallas más comunes.
5.  **Resolución:** El usuario debe ingresar el número correspondiente. El sistema evaluará el stock en tiempo real y:
    * Devolverá un presupuesto automático y un turno formateado omitiendo fines de semana.
    * O alertará una derivación directa al técnico por falta de stock o complejidad de la falla.
