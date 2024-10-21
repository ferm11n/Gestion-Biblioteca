from datetime import datetime

def fechaActual():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#%Y-%m-%d %H:%M:%S Formatea la fecha en un formato las legible
#Año-Mes-Dia Hora:Minutos