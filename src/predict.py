import pandas as pd

def predict_material(model, features: dict):
    X_new = pd.DataFrame([features])
    prediction = model.predict(X_new)[0]
    return prediction