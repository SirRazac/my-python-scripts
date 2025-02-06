# ------------------------------------------------------------------------------
# Import Packages
# ------------------------------------------------------------------------------
from datetime import datetime, timedelta

# -------------------------------------------------------------------------------
# Bestehende Funktionen
# -------------------------------------------------------------------------------
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

# -------------------------------------------------------------------------------
# Neue Funktionen zur Berechnung der Endzeit
# -------------------------------------------------------------------------------
def berechne_endzeit_fuer_arbeitszeit(startzeit, pause_minuten, ziel_arbeitszeit):
    """
    Berechnet die Endzeit, wenn man ab der Startzeit mit einer effektiven
    Arbeitszeit von 'ziel_arbeitszeit' Stunden plus der Pausenzeit arbeitet.
    
    :param startzeit: Startzeit als String im Format "HH:MM"
    :param pause_minuten: Pausenzeit in Minuten (int)
    :param ziel_arbeitszeit: gewünschte effektive Arbeitszeit in Stunden (z.B. 8 oder 9)
    :return: Endzeit als String im Format "HH:MM"
    """
    start = datetime.strptime(startzeit, "%H:%M")
    # Es wird die Pausenzeit (in Minuten) zusätzlich zur effektiven Arbeitszeit (in Stunden) addiert.
    end = start + timedelta(hours=ziel_arbeitszeit, minutes=pause_minuten)
    return end.strftime("%H:%M")

# -------------------------------------------------------------------------------
# Nutzereingaben
# -------------------------------------------------------------------------------
startzeit = input("Gib die Startzeit ein (z.B. 07:00): ")
pause_minuten = int(input("Gib die Pausenzeit in Minuten ein (z.B. 30): "))
endzeit = input("Gib die Endzeit ein (z.B. 15:30): ")

# Bestehende Berechnungen
arbeitszeit_mit_pause = berechne_arbeitszeit(startzeit, endzeit, pause_minuten)
neue_sollzeit = berechne_sollzeit(arbeitszeit_mit_pause)
print(f"Deine neue Sollzeit beträgt: {neue_sollzeit:.2f} Stunden.")

# -------------------------------------------------------------------------------
# Neue Berechnungen: Endzeit für 8 bzw. 9 Stunden effektive Arbeitszeit
# -------------------------------------------------------------------------------
endzeit_8h = berechne_endzeit_fuer_arbeitszeit(startzeit, pause_minuten, 8)
endzeit_9h = berechne_endzeit_fuer_arbeitszeit(startzeit, pause_minuten, 9)

print(f"Um genau 8 Stunden effektive Arbeitszeit zu erreichen, müsstest du bis {endzeit_8h} arbeiten.")
print(f"Um nicht mehr als 9 Stunden effektive Arbeitszeit zu erreichen, kannst du maximal bis {endzeit_9h} arbeiten.")
