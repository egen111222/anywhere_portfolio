from flask import Flask
from models import db
from models import Article
from dotenv import load_dotenv
import os
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DB"]
app.secret_key = os.environ["SECRET_KEY"]
db.init_app(app)
with app.app_context():
    db.create_all()

admin = Admin(app, name='microblog', template_mode='bootstrap3')
admin.add_view(ModelView(Article, db.session))
if __name__ == "__main__":
    app.run()
