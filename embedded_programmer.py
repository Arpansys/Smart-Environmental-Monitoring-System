def recommend_firmware_action(system_report):
    """
    Embedded Programmer Agent:
    Recommends firmware actions based on system status.
    """

    status = system_report["status"]

    if status == "NORMAL":
        action = "Maintain normal monitoring."
        reason = "No active warning detected."

    elif status == "WARNING":
        action = "Activate warning indicators."
        reason = "A sensor has crossed its warning threshold."

    elif status == "ALERT ACKNOWLEDGED":
        action = "Keep warning indicators active."
        reason = "User acknowledged the warning, but the condition remains."

    else:
        action = "Check sensor communication and firmware."
        reason = "System data is invalid or incomplete."

    return {
        "recommended_action": action,
        "reason": reason
    }