from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import text

import mysql.connector
from mysql.connector import Error
from fastapi import FastAPI, UploadFile, File

# SQLALCHEMY_DATABASE_URL  = "mysql+mysqlconnector://root:root@localhost:3306/house"
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
# Base = declarative_base()

connection = mysql.connector.connect(host='localhost',
                                             database='house',
                                             user='root',
                                             password='root')

connection.connect();

app = FastAPI()


# TODO: asosiy sahifaga biror narsa ishlab chiqish kerak

@app.get("/")
async def home():
    return {"message": "House Price Prediction API"}


@app.get("/houses/apartments/id/{id}")
async def house(id: int = 1):

            cursor = connection.cursor()
            sql_query = "select * from appartments as p WHERE p.id={}".format(id)

            print('########', sql_query)

            cursor.execute(sql_query)

            record = cursor.fetchone()

            data = []
            data.append({
                'id': record[0],
                'type_id': record[1],
                'rooms': record[2],
                'bads': record[3],
                'baths': record[4],
                'price': record[5],
            })

            return {"data": data}


@app.post("/houses/apartments/")
async def create_upload_file(file: UploadFile = File(...)):
    import csv

    return {"filename": file.filename}
