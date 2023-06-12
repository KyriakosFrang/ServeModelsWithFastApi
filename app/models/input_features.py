from typing import Tuple

from pydantic import BaseModel, conlist


class InputFeatures(BaseModel):
    features: conlist(item_type=int, min_items=4, max_items=4)  # type: ignore
