import hashlib
import pickle
import random
import string

from sklearn import datasets, svm

classifier = svm.SVC()
X,y = datasets.load_iris(return_X_y=True)
classifier.fit(X,y)
s = pickle.dumps(classifier)


import psycopg2

# PostgreSQL connection details
conn = psycopg2.connect(
    host="localhost",
    database="mydatabase",
    user="myuser",
    password="mypassword"
)

# Create tables for users and models
with conn.cursor() as cursor:
    cursor.execute("""

        DROP table IF EXISTS users;
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username TEXT,
            email TEXT,
            password TEXT
        );
    """)
    cursor.execute("""
        DROP TABLE IF EXISTS models;
        CREATE TABLE IF NOT EXISTS models (
            id SERIAL PRIMARY KEY,
            name TEXT,
            model_data BYTEA
        );
    """)
    conn.commit()

# Dummy users data
users_data = [
    {"username": "user1", "email": "user1@example.com", "password": "password1"},
    {"username": "user2", "email": "user2@example.com", "password": "password2"},
    {"username": "user3", "email": "user3@example.com", "password": "password3"},
]

# Insert dummy users into the database
with conn.cursor() as cursor:
    for user_data in users_data:
        password_hash = hashlib.sha256(user_data["password"].encode()).hexdigest()
        cursor.execute("""
            INSERT INTO users (username, email, password)
            VALUES (%(username)s, %(email)s, %(password)s);
        """, {"username": user_data["username"], "email": user_data["email"], "password": password_hash})
    conn.commit()

# Dummy models data
models_data = [
    {"name": "Model1", "model_data": s},
    {"name": "Model2", "model_data": s},
    {"name": "Model3", "model_data": s},
]

# Insert dummy models into the database
with conn.cursor() as cursor:
    for model_data in models_data:
        cursor.execute("""
            INSERT INTO models (name, model_data)
            VALUES (%(name)s, %(model_data)s);
        """, model_data)
    conn.commit()

# Close the connection
conn.close()
