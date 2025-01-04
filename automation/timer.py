import time
import winsound

def timer(minutes):
    try:
        seconds = minutes * 60
        print(f"Timer startet für {minutes} Minute(n).")

        while seconds > 0:
            mins, secs = divmod(seconds, 60)
            print(f"{mins:02}:{secs:02}", end="\r")
            time.sleep(1)
            seconds -= 1

        print("\nZeit ist um!")
        play_sound()

    except KeyboardInterrupt:
        print("\nTimer abgebrochen.")

def play_sound():
    audio_file = r"D:\\GitHub\\my-python-scripts\\automation\alert.wav"

    try:
        winsound.PlaySound(audio_file, winsound.SND_FILENAME)
    except RuntimeError as e:
        print(f"Fehler beim Abspielen des Tons: {e}")

if __name__ == "__main__":
    try:
        user_input = input("Gib die Zeit in Minuten ein: ")
        minutes = int(user_input)
        if minutes <= 0:
            print("Bitte eine gültige Zahl größer als 0 eingeben.")
        else:
            timer(minutes)
    except ValueError:
        print("Ungültige Eingabe. Bitte eine ganze Zahl eingeben.")
