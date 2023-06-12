from typing import Tuple

from pydantic import BaseModel, conlist


class Prediction(BaseModel):
    prediction: int
