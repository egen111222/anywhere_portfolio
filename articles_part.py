from flask import Blueprint,render_template
from models import Article
from models import db

articles_app = Blueprint('articles_app', __name__,
                         template_folder='templates')

@articles_app.route("/")
def view_articles():
    articles = db.paginate(Article.query,per_page=20)
    return render_template("articles.html",
                           articles=articles)


@articles_app.route("/<article_id>")
def view_article(article_id):
    article = Article.query.filter(Article.id == article_id).first()
    return render_template("article.html",
                           article=article)
