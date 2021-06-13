from flask import Flask,render_template
import os

app = Flask(__name__,static_folder=os.path.abspath("application/view/static"), 
            template_folder=os.path.abspath("application/view/templates"))

@app.route("/", methods=['GET'])
def home():
    return render_template("home.html")
