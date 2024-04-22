from sqlalchemy import Column, DateTime
from sqlalchemy.sql import func
from app import db

class Users(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    user_id = db.Column("user_id", db.String(500))
    name = db.Column("name", db.String(500))
    email = db.Column("email", db.String(500))
    
    Created = Column(DateTime(timezone=True), server_default=func.now())

    def __init__(self, name, email):
        self.name = name
        self.email = email
       

