def diagnose_system(test_results, system_report, firmware_report):
    """
    Debugging Engineer Agent:
    Combines findings from the other three agents.
    """

    failures = [
        result for result in test_results
        if result.startswith("FAIL")
    ]

    if not failures:
        return {
            "diagnosis": "No faults detected",
            "recommendation": "Continue normal system monitoring.",
            "architect_status": system_report["status"],
            "firmware_action": firmware_report["recommended_action"]
        }

    recommendations = []

    for failure in failures:

        if "Temperature" in failure:
            recommendations.append(
                "Check DHT11 wiring, D10 connection and sensor power."
            )

        elif "Humidity" in failure:
            recommendations.append(
                "Inspect DHT11 sensor and data connection."
            )

        elif "Gas" in failure:
            recommendations.append(
                "Check FC-22 power, ground and AO-to-A0 connection."
            )

        elif "Warning logic" in failure:
            recommendations.append(
                "Check warning thresholds and Arduino firmware logic."
            )

        else:
            recommendations.append(
                "Inspect sensor data and communication."
            )

    return {
        "diagnosis": "; ".join(failures),
        "recommendation": " ".join(recommendations),
        "architect_status": system_report["status"],
        "firmware_action": firmware_report["recommended_action"]
    }