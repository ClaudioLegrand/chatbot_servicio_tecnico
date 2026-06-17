# logica_bot.py
import telegram as tg
import base_datos as bd
import turnos

def procesar_ingreso_cliente():
    """Maneja el saludo inicial y el registro de clientes nuevos."""
    tg.enviar_mensaje("¡Hola! Bienvenido al Servicio Técnico de Celulares.")

    dni = tg.recibir_datos("Ingresá tu DNI sin puntos")
    dni = dni.replace(".", "").strip()
    while not dni.isdigit():
        tg.enviar_mensaje("Eso no parece un DNI válido. Ingresá solo números, sin puntos ni espacios.")
        dni = tg.recibir_datos("Ingresá tu DNI sin puntos")
        dni = dni.replace(".", "").strip()
    
    if not bd.buscar_cliente(dni):
        tg.enviar_mensaje("Veo que es tu primera vez consultando con nosotros.")
        nombre = tg.recibir_datos("¿Cómo es tu nombre?")
        bd.guardar_cliente_nuevo(dni, nombre)
        tg.enviar_mensaje(f"¡Un gusto conocerte, {nombre}! Tus datos fueron registrados.")
    
    return dni

def procesar_garantia(dni):
    """Verifica la garantía y asigna turno si corresponde."""
    tg.enviar_mensaje("Aguardá un momento, estoy verificando si tu equipo está en garantía...")
    if bd.verificar_garantia(dni):
        fecha_turno = turnos.generar_turno_fecha()
        bd.generar_ticket(dni, "Garantía", "Turno Asignado")
        tg.enviar_mensaje("¡Buenas noticias! Tu equipo está en garantía.")
        tg.enviar_mensaje(f"Se generó tu ticket. Te esperamos el día: {fecha_turno}. Acercate por el local.")
        return True
    return False

def procesar_presupuesto(dni):
    """Maneja el flujo de presupuestos, stock y derivaciones."""
    tg.enviar_mensaje("El equipo se encuentra fuera de garantía. Vamos a presupuestar la reparación.")
    opcion_falla = tg.mostrar_menu_fallas()
    
    # Ahora las fallas comunes van del 1 al 6
    if opcion_falla in [1, 2, 3, 4, 5, 6]:
        tg.enviar_mensaje("Buscando precio y disponibilidad de repuestos en nuestro sistema...")
        # Pasamos a string para que coincida con el CSV
        datos_repuesto = bd.consultar_stock_y_precio(str(opcion_falla)) 
        
        if datos_repuesto and int(datos_repuesto['cantidad']) > 0:
            precio = datos_repuesto['precio']
            nombre_repuesto = datos_repuesto['repuesto']
            fecha_turno = turnos.generar_turno_fecha()
            
            tg.enviar_mensaje(f"¡Tenemos stock de {nombre_repuesto}! El presupuesto automático es de ${precio}.")
            bd.generar_ticket(dni, "Presupuesto Aprobado", "Esperando equipo")
            tg.enviar_mensaje(f"Se generó tu ticket para reparación rápida. Te esperamos el día: {fecha_turno}.")
        else:
            tg.enviar_mensaje("En este momento NO contamos con stock inmediato para ese repuesto.")
            tg.enviar_mensaje("Estoy derivando tu caso a un técnico para buscar proveedores alternativos...")
            bd.generar_ticket(dni, "Falta Stock", "Derivado a Técnico")
            bd.alertar_tecnico(dni, "Falta de stock para repuesto solicitado.")
            
    else:
        # Falla no común (opción 7)
        tg.enviar_mensaje("Por el tipo de problema, necesitamos hacer una revisión más profunda.")
        tg.enviar_mensaje("Notificando a un técnico para atención personalizada por chat...")
        bd.generar_ticket(dni, "Atención Personalizada", "Derivado a Técnico")
        bd.alertar_tecnico(dni, "Requiere atención personalizada (Falla compleja).")
