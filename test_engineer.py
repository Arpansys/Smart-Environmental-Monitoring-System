def run_system_tests(data):
    """
    Test Engineer Agent:
    Checks sensor data and verifies warning logic.
    """

    results = []

    try:
        temperature = float(data["TEMP"])
        humidity = float(data["HUM"])
        gas = int(data["GAS"])
        warning = int(data["WARNING"])

        # Test 1: Temperature validity
        if -40 <= temperature <= 80:
            results.append("PASS: Temperature reading valid")
        else:
            results.append("FAIL: Abnormal temperature reading")

        # Test 2: Humidity validity
        if 0 <= humidity <= 100:
            results.append("PASS: Humidity reading valid")
        else:
            results.append("FAIL: Abnormal humidity reading")

        # Test 3: Gas sensor reading
        if 0 <= gas <= 1023:
            results.append("PASS: Gas sensor reading valid")
        else:
            results.append("FAIL: Invalid gas sensor reading")

        # Test 4: Warning logic
        expected_warning = (
            temperature >= 35.0 or gas >= 70
        )

        if warning == int(expected_warning):
            results.append("PASS: Warning logic matches test thresholds")
        else:
            results.append("FAIL: Warning logic mismatch")

    except (KeyError, ValueError, TypeError):
        results.append("FAIL: Invalid or incomplete sensor data")

    return results