import mysql.connector
import os
from dotenv import load_dotenv

#Carrega as variaeis do dotenv para os dados nao ficarem expostos
load_dotenv()

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
