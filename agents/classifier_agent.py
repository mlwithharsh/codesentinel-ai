from jedi._compatibility import pickle_load
import pickle
import os

class VulnerabilityClassifier:
    def __init__(self,model_path, vectorizer_path):
        with open (model_path , "rb") as f :
            self.model = pickle.load.load(f)

        with open(vectorizer_path , "rb") as f:
            self.vectorizer = pickle.load(f)

    def predict(self,code_snippet):
        features = self.vectorizer.transform([code_snippet])
        prediction = self.model.predict(features)
        
        if hasattr(self.model , "predict_prob"):
            probability = max(self.model.predict_prob(features)[0])

        else :
            probability = None 

        return {
            "label" : prediction,
            "Confidence" : float(probability) if probability else None
        }
