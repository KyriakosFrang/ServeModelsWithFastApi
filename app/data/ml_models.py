import pickle

import psycopg2
from fastapi import HTTPException
from ..config import config

async def get_model(model_id):
    conn = psycopg2.connect(
        host=config.DATABASE_URL,
        database=config.POSTGRES_DB,
        user=config.POSTGRES_USER,
        password=config.POSTGRES_PASSWORD
    )

    select_query = "SELECT model_data FROM models WHERE id = %s;"
    with conn.cursor() as cursor:
        cursor.execute(select_query, (model_id,))
        result = cursor.fetchone()
        if result:
            serialized_model = result[0]
            return pickle.loads(serialized_model)
        else:
            raise HTTPException(status_code=404, detail="Model not found")
    conn.close()
