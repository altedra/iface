# Model init
from iface.config import app
from flask_mongoalchemy import MongoAlchemy

db = MongoAlchemy(app)

class BaseOU(db.Document):
    name = db.StringField()
    
