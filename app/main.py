from typing import Dict

from fastapi import FastAPI
import numpy as np
from .data.ml_models import get_model

app = FastAPI()

@app.post("/predict/{model_id}")
async def predict(model_id: int, input_data:list):
    model =await  get_model(model_id)
    # Use the loaded model for predictions using the input data
    np_array = np.array(input_data)
    prediction = model.predict(np_array.reshape(1,-1))
    return {"prediction": int(prediction[0])}