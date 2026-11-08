import serial
import time

PORT = "COM3"
BAUD_RATE = 9600

try:
    arduino = serial.Serial(PORT, BAUD_RATE, timeout=2)

    time.sleep(2)

    print("Connected to Arduino!")
    print("Receiving sensor data...\n")

    while True:
        if arduino.in_waiting:
            data = arduino.readline().decode(
                "utf-8", errors="replace"
            ).strip()

            if data:
                print(data)

except serial.SerialException as error:
    print("Could not connect to Arduino:", error)

except KeyboardInterrupt:
    print("\nConnection stopped.")

finally:
    if "arduino" in locals() and arduino.is_open:
        arduino.close()
        print("Arduino connection closed.")