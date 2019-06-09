from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

try:
    client = MongoClient("mongodb://my_db:27017")
    db = client.projectDB
    users = db["Users"]
    users.insert({
        "imie": "Sebastian",
        "mgs": "Moja wiadomosc"
    })
except Exception:
    db = None

import hello_world.views  # noqa