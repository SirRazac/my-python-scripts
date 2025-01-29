# ------------------------------------------------------------------------------
# Import Packages
# ------------------------------------------------------------------------------
from datetime import datetime

def berechne_arbeitszeit(startzeit, endzeit, pause_minuten):
    start = datetime.strptime(startzeit, "%H:%M")
    end = datetime.strptime(endzeit, "%H:%M")
    
    arbeitszeit = (end - start).seconds / 3600
    
    pause = pause_minuten / 60
    arbeitszeit_mit_pause = arbeitszeit - pause
    
    return arbeitszeit_mit_pause

def berechne_sollzeit(arbeitszeit_mit_pause, standard_sollzeit=8):
    neue_sollzeit = standard_sollzeit - (standard_sollzeit - arbeitszeit_mit_pause)
    return neue_sollzeit

startzeit = input("Gib die Startzeit ein (z.B. 07:00): ")
pause_minuten = int(input("Gib die Pausenzeit in Minuten ein (z.B. 30): "))
endzeit = input("Gib die Endzeit ein (z.B. 15:30): ")

arbeitszeit_mit_pause = berechne_arbeitszeit(startzeit, endzeit, pause_minuten)
neue_sollzeit = berechne_sollzeit(arbeitszeit_mit_pause)

print(f"Deine neue Sollzeit beträgt: {neue_sollzeit:.2f} Stunden.")
