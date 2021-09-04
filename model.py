from db import db


class Img(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.Text, unique=True, nullable=False)
    name = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)

    Course_name = db.Column(db.Text, nullable=False)
    Course_link = db.Column(db.Text, nullable=False)
    Course_Descreption = db.Column(db.Text, nullable=False)
    Course_date = db.Column(db.Text, nullable=False)
