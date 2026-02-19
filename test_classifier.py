from agents.classifier_agent import VulnerabilityClassifier
from agents.risk_agent import RiskScorer

classifier = VulnerabilityClassifier(
    model_path="ml/models/final_model.pkl",
    vectorizer_path="ml/models/vectorizer.pkl"
)

risk_agent = RiskScorer()

snippet = "cursor.execute('SELECT * FROM users WHERE id=' + user_id)"

result = classifier.predict(snippet)
risk_result = risk_agent.calculate_risk(
    result["label"],
    result["confidence"]
)

print(risk_result)
