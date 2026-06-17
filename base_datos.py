# base_datos.py
import csv
import os
import datetime

# --- INICIALIZACIÓN DE DATOS DE PRUEBA ---
def inicializar_archivos():
    """Crea los archivos CSV con datos de prueba si no existen en la carpeta."""
    try:
        if not os.path.exists('stock_repuestos.csv'):
            with open('stock_repuestos.csv', mode='w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['id_falla', 'repuesto', 'precio', 'cantidad'])
                writer.writerow(['1', 'Modulo Pantalla', '45000', '5'])
                writer.writerow(['2', 'Bateria', '15000', '0']) 
                writer.writerow(['3', 'Pin de Carga', '8000', '12'])
                writer.writerow(['4', 'Modulo Camara', '22000', '3'])
                writer.writerow(['5', 'Modulo Altavoz/Microfono', '9500', '8'])
                writer.writerow(['6', 'Flex de Botones', '6000', '15'])

        if not os.path.exists('clientes.csv'):
            with open('clientes.csv', mode='w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['dni', 'nombre'])
                
        if not os.path.exists('garantias.csv'):
            with open('garantias.csv', mode='w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['dni', 'estado'])
                writer.writerow(['11111111', 'activa']) # DNI de prueba con garantía

        if not os.path.exists('tickets.csv'):
            with open('tickets.csv', mode='w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['dni', 'tipo_ticket', 'estado'])

        if not os.path.exists('bandeja_tecnico.txt'):
            with open('bandeja_tecnico.txt', mode='w', encoding='utf-8') as f:
                f.write("=== BANDEJA DE ENTRADA - TÉCNICO ===\n")
                f.write("Aquí se registrarán las derivaciones automáticas del Chatbot.\n")
                f.write("-" * 50 + "\n")
                
    except PermissionError:
        print("⚠️ [Base de Datos]: Error de permisos. Asegurate de no tener los archivos CSV abiertos en otro programa (como Excel).")
    except Exception as e:
        print(f"⚠️ [Base de Datos]: Ocurrió un error inesperado al crear los archivos: {e}")

# --- FUNCIONES DE LECTURA Y ESCRITURA ---

def buscar_cliente(dni):
    """Busca si el cliente ya existe en la base de datos."""
    try:
        with open('clientes.csv', mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for fila in reader:
                if fila['dni'] == dni:
                    return True
        return False
    
    except FileNotFoundError:
        print("⚠️ [Base de Datos]: El archivo clientes.csv no existe. Se asume que no hay clientes.")
        return False
    except Exception as e:
        print(f"⚠️ [Base de Datos]: Error al buscar cliente: {e}")
        return False

def guardar_cliente_nuevo(dni, nombre):
    """Agrega un nuevo cliente al CSV."""
    try:
        with open('clientes.csv', mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            # Pasamos una lista, csv.writer se encarga de las comas y el \n al final
            writer.writerow([dni, nombre])
            
    except PermissionError:
        print("⚠️ [Base de Datos]: No se pudo guardar el cliente. Cerrá el archivo clientes.csv si lo tenés abierto.")
    except Exception as e:
        print(f"⚠️ [Base de Datos]: Error al guardar nuevo cliente: {e}")

def verificar_garantia(dni):
    """Verifica si el DNI tiene una garantía activa."""
    try:
        with open('garantias.csv', mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for fila in reader:
                if fila['dni'] == dni and fila['estado'] == 'activa':
                    return True
        return False
    
    except FileNotFoundError:
        print("⚠️ [Base de Datos]: El archivo garantias.csv no fue encontrado.")
        return False
    except Exception as e:
        print(f"⚠️ [Base de Datos]: Error al verificar garantía: {e}")
        return False

def consultar_stock_y_precio(id_falla):
    """Devuelve un diccionario con los datos del repuesto si lo encuentra."""
    try:
        with open('stock_repuestos.csv', mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for fila in reader:
                if fila['id_falla'] == id_falla:
                    return fila 
        return None
    
    except FileNotFoundError:
        print("⚠️ [Base de Datos]: El archivo de stock no existe.")
        return None
    except Exception as e:
        print(f"⚠️ [Base de Datos]: Error al consultar stock: {e}")
        return None

def generar_ticket(dni, tipo_ticket, estado):
    """Guarda el ticket en la base de datos para seguimiento."""
    try:
        with open('tickets.csv', mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([dni, tipo_ticket, estado])

    except PermissionError:
        print("⚠️ [Base de Datos]: No se pudo generar el ticket. El archivo tickets.csv está bloqueado o abierto.")
    except Exception as e:
        print(f"⚠️ [Base de Datos]: Error al generar el ticket: {e}")

# FUNCION PARA NOTIFICAR AL TECNICO

def alertar_tecnico(dni_cliente, motivo):
    """
    Simula el envío de un correo/alerta al técnico guardando 
    el requerimiento en un archivo de texto (Bandeja de entrada).
    """
    fecha_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    mensaje_alerta = f"[{fecha_hora}] URGENTE - Cliente DNI: {dni_cliente} | Motivo: {motivo}\n"
    
    try:
        with open('bandeja_tecnico.txt', mode='a', encoding='utf-8') as f:
            f.write(mensaje_alerta)
        print(f"✅ [Sistema]: Se ha notificado al técnico exitosamente (Log guardado).")
        
    except Exception as e:
        print(f"⚠️ [Sistema]: Error al intentar notificar al técnico: {e}")