def risk_level(score):
    if score >= 75:
        return "HIGH"
    elif score >= 40:
        return "MEDIUM"
    return "LOW"
