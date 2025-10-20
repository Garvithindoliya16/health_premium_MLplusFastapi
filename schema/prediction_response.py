from pydantic import BaseModel, Field
from typing import Dict

class PredictionResponse(BaseModel):
    predicted_category:str=Field(...,description="The Predicted insurance premium category",examples=["High"])

    confidence:float=Field(...,description="Model's confidence score for the predicted class range(0 to 1)",examples=[0.456])

    class_probabilities:Dict[str,float]=Field(...,description="Probability distribution across all possible classes",examples=[{"High": 0.41,"Low": 0.13,"Medium": 0.46}])

