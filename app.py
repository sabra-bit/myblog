
from flask import Flask, request, Response, render_template
from flask.templating import DispatchingJinjaLoader
from werkzeug.utils import secure_filename
import calendar
from datetime import datetime
import pytz 
from db import db_init, db
from model import Img

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data_store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db_init(app)

@app.route('/adminLog', methods=['POST'])
def adminLog():
    name = request.form["user"]
    link = request.form["password"]
    print(name)
    if name == "sabra" and link == "122":
    
        return render_template("index.html")
    else:
        return "not allowd"


@app.route('/Delete', methods=['POST'])
def admindelete():
    namex = request.form["post"]
    user= Img.query.filter(Img.id == namex).delete()
    
    db.session.commit()

    return "post deleted"
    
@app.route('/dele', methods=['POST','GET'])
def dele():
    img = Img.query.all()
    
    return render_template("posts.html",x=img)


@app.route('/admin')
def admin():
    
    return render_template("log.html")

@app.route('/')
def hello_world1():
    img = Img.query.all()
    # x = str(1)
    return render_template("view.html",x=img)

@app.route('/upload', methods=['POST'])
def upload():
    name = request.form["name"]
    link = request.form["link"]
    desc = request.form["descrption"]
    now = datetime.now(pytz.timezone('Africa/Cairo')) # you could pass `timezone` object here
    link = "https://www.youtube.com/embed/"+link 
    date = str(now.strftime("%m/%d/%Y, %H:%M:%S"))
     
    pic = request.files['pic']
    if not pic:
        return 'No pic uploaded!', 400

    filename = secure_filename(pic.filename)
    mimetype = pic.mimetype
    if not filename or not mimetype:
        return 'Bad upload!', 400

    img = Img(img=pic.read(), name=filename, mimetype=mimetype,Course_name=name,Course_link=link,Course_Descreption=desc,Course_date=date)
    db.session.add(img)
    db.session.commit()

    return 'Course Uploaded!', 200


@app.route('/img/<int:id>')
def get_img(id):
    img = Img.query.filter_by(id=id).first()
    if not img:
        return 'Img Not Found!', 404
    
    
    return Response(img.img, mimetype=img.mimetype)
@app.route('/post/<int:id>')
def Post(id):
    img = Img.query.filter_by(id=id).first()
    if not img:
        return 'Img Not Found!', 404
    
    
    return render_template("singlePost.html",post=img)

if __name__ == "__main__":
   app.run(debug=True)
 