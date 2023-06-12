from fastapi import Depends, FastAPI

from .db.postgress import get_connection
from .dependencies import verify_api_key
from .models.input_features import InputFeatures
from .models.prediction import Prediction
from .services import predict as predict_service

app = FastAPI(title="Tutorial", version="0.0.1", dependencies=[Depends(verify_api_key)])


@app.post("/predict/{model_id}", response_model=Prediction)
async def predict(model_id: int, input_data: InputFeatures, db=Depends(get_connection)):
    return predict_service.predict(
        model_id=model_id, input_data=input_data, db=db
    ).dict()
