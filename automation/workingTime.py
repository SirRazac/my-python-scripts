# ------------------------------------------------------------------------------
# Import Packages
# ------------------------------------------------------------------------------
from datetime import datetime, timedelta

# -------------------------------------------------------------------------------
# Bestehende Funktionen
# -------------------------------------------------------------------------------
def berechne_arbeitszeit(startzeit, endzeit, pause_minuten):
    """
    Berechnet die effektive Arbeitszeit (in Stunden), indem die Pause abgezogen wird.
    """
    start = datetime.strptime(startzeit, "%H:%M")
    end = datetime.strptime(endzeit, "%H:%M")
    
    # Berechnung der reinen Arbeitszeit (in Stunden)
    arbeitszeit = (end - start).seconds / 3600
    
    # Umrechnung der Pause in Stunden und Abzug von der Arbeitszeit
    pause = pause_minuten / 60
    arbeitszeit_mit_pause = arbeitszeit - pause
    
    return arbeitszeit_mit_pause

def berechne_sollzeit(arbeitszeit_mit_pause, standard_sollzeit=8):
    """
    Hier wird aktuell nur die effektive Arbeitszeit zurückgegeben.
    Bei Bedarf kann die Logik erweitert werden.
    """
    neue_sollzeit = standard_sollzeit - (standard_sollzeit - arbeitszeit_mit_pause)
    return neue_sollzeit

# -------------------------------------------------------------------------------
# Neue Funktion zur Berechnung der Endzeit
# -------------------------------------------------------------------------------
def berechne_endzeit_fuer_arbeitszeit(startzeit, pause_minuten, ziel_arbeitszeit):
    """
    Berechnet die Endzeit, wenn ab der Startzeit mit einer effektiven
    Arbeitszeit von 'ziel_arbeitszeit' Stunden plus Pausenzeit gearbeitet wird.
    
    :param startzeit: Startzeit als String im Format "HH:MM"
    :param pause_minuten: Pausenzeit in Minuten (int)
    :param ziel_arbeitszeit: Gewünschte effektive Arbeitszeit in Stunden (z.B. 8 oder 9)
    :return: Endzeit als String im Format "HH:MM"
    """
    start = datetime.strptime(startzeit, "%H:%M")
    end = start + timedelta(hours=ziel_arbeitszeit, minutes=pause_minuten)
    return end.strftime("%H:%M")

# -------------------------------------------------------------------------------
# Hauptprogramm mit Auswahlmenü
# -------------------------------------------------------------------------------
def main():
    while True:
        print("\nWähle eine Option:")
        print("1: Berechne Arbeitszeit und Sollzeit")
        print("2: Berechne Endzeit für genau 8 Stunden effektive Arbeitszeit")
        print("3: Berechne Endzeit für maximal 9 Stunden effektive Arbeitszeit")
        print("4: Programm beenden")
        
        auswahl = input("Deine Auswahl (1-4): ")
        
        if auswahl == "1":
            # Option 1: Berechnung der effektiven Arbeitszeit und der Sollzeit
            startzeit = input("Gib die Startzeit ein (z.B. 07:00): ")
            pause_minuten = int(input("Gib die Pausenzeit in Minuten ein (z.B. 30): "))
            endzeit = input("Gib die Endzeit ein (z.B. 15:30): ")
            
            arbeitszeit_mit_pause = berechne_arbeitszeit(startzeit, endzeit, pause_minuten)
            neue_sollzeit = berechne_sollzeit(arbeitszeit_mit_pause)
            
            print(f"\nDeine effektive Arbeitszeit beträgt: {arbeitszeit_mit_pause:.2f} Stunden.")
            print(f"Deine neue Sollzeit beträgt: {neue_sollzeit:.2f} Stunden.")
        
        elif auswahl == "2":
            # Option 2: Berechnung der Endzeit für 8 Stunden effektive Arbeitszeit
            startzeit = input("Gib die Startzeit ein (z.B. 07:00): ")
            pause_minuten = int(input("Gib die Pausenzeit in Minuten ein (z.B. 30): "))
            
            endzeit_8h = berechne_endzeit_fuer_arbeitszeit(startzeit, pause_minuten, 8)
            print(f"\nUm genau 8 Stunden effektive Arbeitszeit zu erreichen, müsstest du bis {endzeit_8h} arbeiten.")
        
        elif auswahl == "3":
            # Option 3: Berechnung der Endzeit für maximal 9 Stunden effektive Arbeitszeit
            startzeit = input("Gib die Startzeit ein (z.B. 07:00): ")
            pause_minuten = int(input("Gib die Pausenzeit in Minuten ein (z.B. 30): "))
            
            endzeit_9h = berechne_endzeit_fuer_arbeitszeit(startzeit, pause_minuten, 9)
            print(f"\nUm nicht mehr als 9 Stunden effektive Arbeitszeit zu erreichen, kannst du maximal bis {endzeit_9h} arbeiten.")
        
        elif auswahl == "4":
            # Option 4: Programm beenden
            print("Programm wird beendet.")
            break
        
        else:
            print("Ungültige Auswahl! Bitte wähle eine Option von 1 bis 4.")

if __name__ == "__main__":
    main()
