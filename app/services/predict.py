import numpy as np

from ..actions.models import get_model
from ..models.input_features import InputFeatures
from ..models.prediction import Prediction


def predict(input_data: InputFeatures, model_id: int, db) -> Prediction:
    model = get_model(db=db, model_id=model_id)
    # Use the loaded model for predictions using the input data
    np_array = np.array(input_data.features)
    prediction = model.predict(np_array.reshape(1, -1))
    return Prediction(prediction=int(prediction[0]))
