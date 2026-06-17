# main.py
import base_datos as bd
import logica_bot

def iniciar_bot():
    # 1. Preparamos el entorno (crea CSVs si no existen)
    bd.inicializar_archivos()
    
    # 2. Saludo, solicitud de datos y registro
    dni_cliente = logica_bot.procesar_ingreso_cliente()
    
    # 3. Flujo principal: Verificar garantía
    tiene_garantia = logica_bot.procesar_garantia(dni_cliente)
    
    # 4. Si no tiene garantía, pasa a la cotización
    if not tiene_garantia:
        logica_bot.procesar_presupuesto(dni_cliente)

if __name__ == "__main__":
    iniciar_bot()