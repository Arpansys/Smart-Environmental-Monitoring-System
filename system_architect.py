def analyze_system(data):
    """
    System Architect Agent:
    Interprets sensor readings and identifies system status.
    """

    try:
        temperature = float(data["TEMP"])
        humidity = float(data["HUM"])
        gas = int(data["GAS"])
        warning = int(data["WARNING"])
        acknowledged = int(data["ACK"])

    except (KeyError, ValueError, TypeError):
        return {
            "status": "INVALID DATA",
            "message": "Incomplete or invalid sensor readings"
        }

    if warning == 1 and acknowledged == 1:
        status = "ALERT ACKNOWLEDGED"
        message = "Warning detected and acknowledged by user."

    elif warning == 1:
        status = "WARNING"
        message = "Environmental warning detected!"

    else:
        status = "NORMAL"
        message = "Environmental conditions within demo thresholds."

    return {
        "status": status,
        "message": message,
        "temperature": temperature,
        "humidity": humidity,
        "gas": gas
    }