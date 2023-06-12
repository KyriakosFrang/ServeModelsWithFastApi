import psycopg2
from ..config import config


async def get_connection():
    return psycopg2.connect(
        host=config.DATABASE_URL,
        database=config.POSTGRES_DB,
        user=config.POSTGRES_USER,
        password=config.POSTGRES_PASSWORD,
    )
