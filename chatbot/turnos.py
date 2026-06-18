# turnos.py
import datetime
import csv
import os

def inicializar_agenda():
    """Crea el archivo de la agenda si no existe."""
    try:
        if not os.path.exists('chatbot/base_de_datos/agenda.csv'):
            with open('chatbot/base_de_datos/agenda.csv', mode='w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['fecha', 'hora'])
                
    except Exception as e:
        print(f"⚠️ [Agenda]: Error al crear agenda.csv: {e}")

def horario_esta_disponible(fecha, hora):
    """Lee el CSV para verificar si esa fecha y hora ya están ocupadas."""
    try:
        with open('chatbot/base_de_datos/agenda.csv', mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for fila in reader:
                if fila['fecha'] == fecha and fila['hora'] == hora:
                    return False # El turno está ocupado
        return True # El turno está libre
    except FileNotFoundError:
        return True

def guardar_turno(fecha, hora):
    """Guarda el turno ocupado en la agenda."""
    try:
        with open('chatbot/base_de_datos/agenda.csv', mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([fecha, hora])
    except Exception as e:
        print(f"⚠️ [Agenda]: Error al guardar el turno: {e}")

def generar_turno_fecha():
    """
    Genera un turno buscando el primer horario disponible.
    Si el día está lleno, avanza al siguiente día hábil.
    """
    inicializar_agenda()
    
    hoy = datetime.date.today()
    dias_espera = 2 
    fecha_turno = hoy + datetime.timedelta(days=dias_espera)
    
    # Lista de horarios de atención del local
    horarios_atencion = ["09:00", "10:00", "11:00", "12:00", "14:00", "15:00", "16:00", "17:00"]
    
    # Bucle infinito hasta que logre encontrar un turno libre y retornarlo
    while True:
        # 1. Validamos que no sea fin de semana
        if fecha_turno.weekday() == 5: # Sábado
            fecha_turno += datetime.timedelta(days=2) # Pasa al Lunes
        elif fecha_turno.weekday() == 6: # Domingo
            fecha_turno += datetime.timedelta(days=1) # Pasa al Lunes
            
        fecha_formateada = fecha_turno.strftime("%d/%m/%Y")
        
        # 2. Buscamos un horario libre en ese día
        for hora in horarios_atencion:
            if horario_esta_disponible(fecha_formateada, hora):
                # Encontramos un hueco, lo guardamos para que nadie más lo use
                guardar_turno(fecha_formateada, hora)
                return f"{fecha_formateada} a las {hora} hs"
        
        # 3. Si el bucle 'for' termina sin retornar nada, significa que TODOS
        # los horarios de ese día están ocupados. Sumamos un día y el 'while' vuelve a empezar.
        fecha_turno += datetime.timedelta(days=1)