import pickle
import pandas as pd

#import the ML model
with open('model/model.pkl','rb') as f:
    model = pickle.load(f)

#MLflow
MODEL_VERSION = '1.0.0'

class_label = model.classes_.tolist()

def predict_output(user_input:dict):

    df=pd.DataFrame([user_input])

    #predict the class
    predicted_class = model.predict(df)[0]

    # Get probabilities for all the classes
    probabilities = model.predict_proba(df)[0]
    confidence = max(probabilities)

    #create mapping: {class_name:probability}
    class_probs = dict(zip(class_label,map(lambda p:round(p,4),probabilities)))
    
    return {
        "predicted_category":predicted_class,
        "confidence":round(confidence,4),
        "class_probabilities":class_probs
    }