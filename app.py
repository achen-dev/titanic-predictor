from flask import Flask, redirect, render_template, request, url_for
import numpy
from joblib import dump, load
from sklearn.naive_bayes import CategoricalNB

app = Flask(__name__)
MODEL = "cnbmodel"

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        user = {}
        user['name'] = request.form["Name"]
        user['age'] = request.form["Age"]
        user['gender'] = request.form["Gender"]
        user['parch'] = request.form["ParCh"]
        user['sibsp'] = request.form["SibSp"]
        user['fare'] = request.form["Fare"]
        return redirect(url_for("index", user=user))
    user = request.args.get("user")
    print(eval(user))
    user = eval(user)
    return render_template("index.html", user=user)

