from application import db

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    timeNeeded = db.Column(db.Integer, nullable=False)
    instructions = db.Column(db.String(1000), nullable=False)
    #MUISTA LISÄTÄ TÄNNE MYÖHEMMIN MYÖS FOREIGN KEYT USER_ID (JA COURSE_ID!)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, name, timeNeeded, instructions):
        self.name = name
        self.timeNeeded = timeNeeded
        self.instructions = instructions
