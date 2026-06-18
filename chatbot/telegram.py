# telegram.py

def enviar_mensaje(mensaje):
    """Simula el envío de un mensaje del bot al cliente en Telegram."""
    print(f"🤖 [Chatbot]: {mensaje}")

def recibir_datos(texto_prompt):
    """Simula la recepción de un mensaje escrito por el cliente."""
    while True:
        entrada = input(f"👤 [Cliente - {texto_prompt}]: ").strip()

        if entrada != "":
            return entrada
        
        print("⚠️  La entrada no puede estar vacía. Por favor, escribí algo.")

def mostrar_menu_fallas():
    """Despliega el menú de opciones y retorna la elección del usuario."""
    enviar_mensaje("¿Cuál parece ser el problema de tu equipo?\n")
    print("   1. Pantalla rota / No da imagen")
    print("   2. La batería dura poco / No enciende")
    print("   3. No carga (Pin de carga)")
    print("   4. Cámara (frontal/trasera) rota")
    print("   5. Micrófono o altavoz no funciona")
    print("   6. Botones (encendido/volumen) trabados")
    print("   7. Otro problema / No estoy seguro\n")

    while True:
        entrada = recibir_datos("Ingresá el número de la opción (1-7)")
        
        try:
            # Intentamos convertir la entrada a un número entero
            opcion = int(entrada)
            
            # Verificamos que el número esté en el rango del menú
            if 1 <= opcion <= 7:
                print("\n")
                return opcion
            else:
                print("⚠️  Ese número no está en el menú. Elegí una opción del 1 al 7.")
                
        except ValueError:
            # Si int() falla porque el usuario escribió letras, se ejecuta esto:
            print("⚠️  Entrada inválida. Por favor, ingresá solo el número de la opción (ejemplo: 1).")

def recibir_dni():
    """
    Solicita el DNI y valida que contenga únicamente números.
    Mantiene al usuario en un bucle hasta que ingrese un dato válido.
    """
    while True:
        dni = recibir_datos("Ingresá tu DNI sin puntos ni espacios")
        
        # .isdigit() verifica que TODOS los caracteres sean números (0-9)
        if dni.isdigit():
            print("\n")
            return dni 
        else:
            print("⚠️  Entrada inválida. El DNI debe contener SOLO números (sin puntos, comas, ni letras). Intentá de nuevo.")

def recibir_nombre():
    """
    Solicita el nombre y valida que contenga únicamente letras y espacios.
    """
    while True:
        nombre = recibir_datos("¿Cómo es tu nombre?")

        if nombre.replace(" ", "").isalpha():
            print("\n")
            return nombre
        else:
            print("⚠️  Entrada inválida. El nombre solo puede contener letras. Intentá de nuevo.")