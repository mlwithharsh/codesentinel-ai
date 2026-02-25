from agents.classifier_agent import VulnerabilityClassifier
from agents.risk_agent import RiskScorer
from agents.patch_agent import PatchGenerator

class CodeSentinelOrchestrator:

    def __init__(self):
        self.classifier = VulnerabilityClassifier(
            model_path="ml/models/final_model.pkl",
            vectorizer_path="ml/models/vectorizer.pkl"
        )
        self.risk_agent = RiskScorer()
        self.patch_agent = PatchGenerator()

    def analyze_code(self, code_snippet):

        # Step 1: Classification
        classification = self.classifier.predict(code_snippet)

        # Step 2: Risk scoring
        risk = self.risk_agent.calculate_risk(
            classification["label"],
            classification["confidence"]
        )

        # Step 3: Patch recommendation
        patch = self.patch_agent.generate_patch(
            code_snippet,
            risk["label"]
        )

        # Step 4: Build structured report
        report = {
            "label": risk["label"],
            "confidence": risk["confidence"],
            "risk_score": risk["risk_score"],
            "severity": risk["severity"],
            "patch": patch
        }

        return report