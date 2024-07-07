from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


 # db intitialized here
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(app)
#db.init_app(app)

#we can do this using MYSQL also, for simplicity we will do it using sqlite here. 
#//// is absolute path, /// is relative path.

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(250), nullable = False) #nullable = false means this cannot be left blank
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' %self.id

#lets create an index route using app route decorator 
@app.route('/') #url string of our route 
def index(): #this is the function for that route 
    return render_template("index.html") #and we do not need to specify the folder the name is templates for a reason 

if __name__ == "__main__":
    app.run(debug=True) #so that if we have any errors they will pop up on the page 

    #accha down below in the console as we see debugger pin is active, we know that it is automatically updating.