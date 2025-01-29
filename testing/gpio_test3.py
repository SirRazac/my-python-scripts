import Adafruit_DHT

# Sensor-Typ und GPIO-Pin definieren
sensor = Adafruit_DHT.DHT22
gpio_pin = 22  

print("Starte DHT22-Sensorabfrage...")

try:
    while True:
        # Sensor abfragen
        humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio_pin)

        if humidity is not None and temperature is not None:
            print(f"Temperatur: {temperature:.1f}°C, Luftfeuchtigkeit: {humidity:.1f}%")
        else:
            print("Fehler beim Lesen des Sensors. Überprüfe die Verkabelung.")

except KeyboardInterrupt:
    print("\nAbbruch durch Benutzer.")
