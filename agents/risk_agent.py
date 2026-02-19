class RiskScorer:
    def __init__(self):
        self.base_severity={
            "SQLi": 9,
            "CommandInjection": 9,
            "Hardcoded": 7,
            "Safe": 1,
            "Suspicious": 5
        }

    def calculate_risk(self, label, confidence):
        base = self.base_severity.get(label, 5)
        if confidence is None:
            confidence = 0.5
        risk_score = base * confidence
        risk_score = round(min(risk_score, 10), 2)
        severity_level = self._map_severity_level(risk_score)
        return {
            "label": label,
            "confidence": confidence,
            "risk_score": risk_score,
            "severity": severity_level
            }


    def _map_severity_level(self, score):
        if score >= 8:
            return "Critical"
        elif score >= 6:
            return "High"
        elif score >= 4:
            return "Medium"
        elif score >= 2:
            return "Low"
        else:
            return "Informational"
