# ------------------------------------------------------------------------------
# Import Packages
# ------------------------------------------------------------------------------
from datetime import datetime, timedelta

# -------------------------------------------------------------------------------
# Funktionen
# -------------------------------------------------------------------------------
def berechne_arbeitszeit(startzeit, endzeit, pause_minuten):
    start = datetime.strptime(startzeit, "%H:%M")
    end = datetime.strptime(endzeit, "%H:%M")
    arbeitszeit = (end - start).seconds / 3600
    pause = pause_minuten / 60
    return arbeitszeit - pause

def berechne_sollzeit(arbeitszeit_mit_pause, standard_sollzeit=8):
    return standard_sollzeit - (standard_sollzeit - arbeitszeit_mit_pause)

def berechne_endzeit_fuer_arbeitszeit(startzeit, pause_minuten, ziel_arbeitszeit):
    start = datetime.strptime(startzeit, "%H:%M")
    end = start + timedelta(hours=ziel_arbeitszeit, minutes=pause_minuten)
    return end.strftime("%H:%M")

# -------------------------------------------------------------------------------
# Hauptprogramm mit Auswahlmenü
# -------------------------------------------------------------------------------
startzeit = input("Gib die Startzeit ein (z.B. 07:00): ")
pause_minuten = int(input("Gib die Pausenzeit in Minuten ein (z.B. 30): "))

while True:
    print("\nWähle eine Option:")
    print("1: Sollzeit/Arbeitszeit berechnen")
    print("2: Berechne Endzeit für 8 und 9 Stunden Arbeitszeit")
    print("3: Beenden")
    
    auswahl = input("Deine Auswahl (1-3): ")
    
    if auswahl == "1":
        endzeit = input("Gib die Endzeit ein (z.B. 15:30): ")
        arbeitszeit = berechne_arbeitszeit(startzeit, endzeit, pause_minuten)
        sollzeit = berechne_sollzeit(arbeitszeit)
        print(f"\nDeine effektive Arbeitszeit beträgt: {arbeitszeit:.2f} Stunden.")
        print(f"Deine neue Sollzeit beträgt: {sollzeit:.2f} Stunden.")
    
    elif auswahl == "2":
        endzeit_8h = berechne_endzeit_fuer_arbeitszeit(startzeit, pause_minuten, 8)
        endzeit_9h = berechne_endzeit_fuer_arbeitszeit(startzeit, pause_minuten, 9)
        print(f"\nUm genau 8 Stunden effektiv zu arbeiten, müsstest du bis {endzeit_8h} arbeiten.")
        print(f"Um genau 9 Stunden effektiv zu arbeiten, müsstest du bis {endzeit_9h} arbeiten.")
    
    elif auswahl == "3":
        print("Programm wird beendet.")
        break
    
    else:
        print("Ungültige Auswahl! Bitte wähle eine Option von 1 bis 3.")
