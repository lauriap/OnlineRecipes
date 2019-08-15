from application import db

from sqlalchemy.sql import text

class User(db.Model):

    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    recipes = db.relationship("Recipe", backref='recipe', lazy=True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    @staticmethod
    def list_top_contributors():
        stmt = text("SELECT Account.id, Account.name, COUNT(Recipe.id) FROM Account"
                    " LEFT JOIN Recipe ON Recipe.account_id = Account.id"
                    " GROUP BY account.id, account.name;")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[1], "recipecount":row[2]})

        return response
