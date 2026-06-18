# main.py
import base_datos as bd
import logica_bot as logica_bot

def iniciar_bot():
    # 1. Preparamos el entorno
    bd.inicializar_archivos()
    
    # 2. Saludo, solicitud de datos y registro
    dni_cliente = logica_bot.procesar_ingreso_cliente()
    
    # 3. MÁQUINA DE ESTADOS: Verificamos si ya tiene un trámite en curso
    tiene_tramite_previo = logica_bot.verificar_estado_previo(dni_cliente)

    # 4. Si NO tiene un trámite previo, arranca el flujo normal
    if not tiene_tramite_previo:
        
        # Verificar garantía
        tiene_garantia = logica_bot.procesar_garantia(dni_cliente)
        
        print("\n")

        # Si no tiene garantía, pasa a la cotización
        if not tiene_garantia:
            logica_bot.procesar_presupuesto(dni_cliente)

if __name__ == "__main__":
    iniciar_bot()