from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo 
from flask_app.models.ninja import Ninja


@app.route("/dojos")
def index():
    dojos = Dojo.get_all()
    return render_template("index.html", dojos = dojos)

@app.route("/create", methods=["POST"])
def create():
    data = {
        "name": request.form['dojoname'],
    }
    Dojo.create(data)
    return redirect("/dojos")

@app.route("/dojos/<int:id>")
def one_dojo(id):
    data={
        "id":id
    }
    return render_template("/dojos.html",dojo=Dojo.dojo_and_ninjas(data)) 

