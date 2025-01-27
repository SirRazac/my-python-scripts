import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Liste aller GPIO-Pins (ohne 3.3V, GND, oder andere reservierte Pins)
gpio_pins = [17, 18, 22, 23, 24, 25, 5, 6, 12, 13, 19, 16, 26, 20, 21]

try:
    print("Starte GPIO-Funktionstest...")

    for pin in gpio_pins:
        print(f"Prüfe GPIO{pin}...")

        # Pin als Ausgang definieren und Signal setzen
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(0.1)

        # Pin als Eingang definieren und Signal prüfen
        GPIO.setup(pin, GPIO.IN)
        if GPIO.input(pin):
            print(f"GPIO{pin}: Funktioniert!")
        else:
            print(f"GPIO{pin}: Keine Funktion erkannt!")

        # Pin zurücksetzen
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
        GPIO.setup(pin, GPIO.IN)

    print("Funktionstest abgeschlossen.")

finally:
    GPIO.cleanup()
    print("Pins zurückgesetzt.")
