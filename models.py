from flask_sqlalchemy import SQLAlchemy
import uuid

db = SQLAlchemy()

class Article(db.Model):
    __tablename__ = "articles"
    id = db.Column(db.String,
                   primary_key=True,
                   default=lambda:str(uuid.uuid4()))
    title = db.Column(db.String(100))
    descritpion = db.Column(db.String(200))
    text = db.Column(db.Text)
