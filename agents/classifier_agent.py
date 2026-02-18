from jedi._compatibility import pickle_load
import pickle
import os

class VulnerabilityClassifier:
    def __init__(self,model_path, vectorizer_path):
        with open (model_path , "rb") as f :
            self.model = pickle.load(f)

        with open(vectorizer_path , "rb") as f:
            self.vectorizer = pickle.load(f)

    def predict(self,code_snippet):
        features = self.vectorizer.transform([code_snippet])
        prediction = self.model.predict(features)[0]
        
        probability = None
        if hasattr(self.model, "predict_proba"):
            proba = self.model.predict_proba(features)[0]
            probability = float(max(proba))

        else :
            probability = None 

        return {
            "label" : prediction,
            "Confidence" : probability
        }
