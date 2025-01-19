import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

output_pins = [17, 22, 5]
input_pins = [18, 23, 6]

for pin in output_pins:
    GPIO.setup(pin, GPIO.OUT)
for pin in input_pins:
    GPIO.setup(pin, GPIO.IN)

try:
    print("Starte Test...")
    for i, (out_pin, in_pin) in enumerate(zip(output_pins, input_pins)):
        print(f"Teste Ausgang GPIO{out_pin} → Eingang GPIO{in_pin}")

        GPIO.output(out_pin, GPIO.HIGH)
        time.sleep(0.5)

        if GPIO.input(in_pin):
            print(f"Durchgang {i + 1}: Signal erkannt!")
        else:
            print(f"Durchgang {i + 1}: Kein Signal erkannt!")

        GPIO.output(out_pin, GPIO.LOW)
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Test unterbrochen.")

finally:
    GPIO.cleanup()
    print("Pins zurückgesetzt.")
