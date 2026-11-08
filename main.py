import serial
import time

from system_architect import analyze_system
from embedded_programmer import recommend_firmware_action
from test_engineer import run_system_tests
from debugging_engineer import diagnose_system
from ai_assistant import ask_gemini


PORT = "COM3"
BAUD_RATE = 9600

SIMULATE_FAULT = False
ai_alert_sent = False


def parse_sensor_data(line):
    data = {}

    try:
        for item in line.split(","):
            key, value = item.split(":", 1)
            data[key.strip()] = value.strip()

        required = ["TEMP", "HUM", "GAS", "WARNING", "ACK"]

        if not all(key in data for key in required):
            return None

        return data

    except ValueError:
        return None


try:
    arduino = serial.Serial(PORT, BAUD_RATE, timeout=2)
    time.sleep(2)

    print("Connected to Arduino!")
    print("FOUR ENGINEERING AGENTS ONLINE\n")

    while True:

        line = arduino.readline().decode(
            "utf-8", errors="replace"
        ).strip()

        if not line:
            continue

        data = parse_sensor_data(line)

        if data is None:
            continue

        # Create a separate copy for agent testing
        agent_data = data.copy()

        # Software fault injection
        if SIMULATE_FAULT:
            agent_data["GAS"] = "2000"

        # Run all four agents
        result = analyze_system(agent_data)
        firmware = recommend_firmware_action(result)
        tests = run_system_tests(agent_data)
        debug = diagnose_system(tests, result, firmware)

        # Identify failed tests
        failures = [
            test for test in tests
            if test.startswith("FAIL")
        ]

        # SYSTEM ARCHITECT REPORT
        print("\n" + "=" * 45)
        print("SYSTEM ARCHITECT REPORT")
        print("Status:", result["status"])
        print("Message:", result["message"])

        if "temperature" in result:
            print("Temperature:", result["temperature"], "C")
            print("Humidity:", result["humidity"], "%")
            print("Gas reading:", result["gas"])

        # EMBEDDED PROGRAMMER REPORT
        print("\nEMBEDDED PROGRAMMER REPORT")
        print("Recommended action:", firmware["recommended_action"])
        print("Reason:", firmware["reason"])

        # TEST ENGINEER REPORT
        print("\nTEST ENGINEER REPORT")

        for test in tests:
            print(test)

        # DEBUGGING ENGINEER REPORT
        print("\nDEBUGGING ENGINEER REPORT")
        print("Diagnosis:", debug["diagnosis"])
        print("Recommendation:", debug["recommendation"])
        print("Architect status:", debug["architect_status"])
        print("Firmware recommendation:", debug["firmware_action"])

        # GEMINI AI CONSULTATION
        if failures and not ai_alert_sent:

            print("\n" + "=" * 45)
            print("GEMINI AI ENGINEER CONSULTATION")
            print("=" * 45)

            diagnostic_report = f"""
            SYSTEM ARCHITECT:
            {result}

            EMBEDDED PROGRAMMER:
            {firmware}

            TEST ENGINEER:
            {tests}

            DEBUGGING ENGINEER:
            {debug}

            ACTUAL ARDUINO SENSOR DATA:
            {data}

            AGENT TEST DATA:
            {agent_data}

            TEST FAILURES:
            {failures}
            """

            ai_result = ask_gemini(diagnostic_report)

            print("\nGEMINI AI DIAGNOSIS:")
            print(ai_result)

            ai_alert_sent = True

        elif not failures:
            ai_alert_sent = False


except serial.SerialException as error:
    print("Serial connection error:", error)

except KeyboardInterrupt:
    print("\nSystem stopped.")

finally:
    if "arduino" in locals() and arduino.is_open:
        arduino.close()
        print("Arduino connection closed.")