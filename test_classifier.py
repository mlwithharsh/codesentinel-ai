from agents.classifier_agent import VulnerabilityClassifier


classifier = VulnerabilityClassifier(
    model_path="ml/models/final_model.pkl",
    vectorizer_path="ml/models/vectorizer.pkl"
)



# test_code = "password = os.getenv('DB_PASSWORD')"
# result = classifier.predict(test_code)

# print(result)
print(classifier.predict("password = 'admin123'"))
print(classifier.predict("os.system('rm -rf ' + user_input)"))
print(classifier.predict("cursor.execute('SELECT * FROM users WHERE id=' + user_id)"))
print(classifier.predict("password = os.getenv('DB_PASSWORD')"))
