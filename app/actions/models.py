import pickle
from fastapi import HTTPException


def get_model(db, model_id: int):
    select_query = "SELECT model_data FROM models WHERE id = %s;"
    with db.cursor() as cursor:
        cursor.execute(select_query, (model_id,))
        result = cursor.fetchone()
        if result:
            serialized_model = result[0]
            return pickle.loads(serialized_model)
        else:
            raise HTTPException(status_code=404, detail="Model not found")
    db.close()
