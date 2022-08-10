from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.ninja import  Ninja
from flask_app.models.dojo import Dojo 

@app.route("/addninja")
def add_ninja():
    dojos = Dojo.get_all()
    return render_template("addninja.html", dojos=dojos)

@app.route("/createninja", methods=["POST"])
def create_ninja():
    data = {
        "dojo": request.form['dojo'],
        "fname": request.form['fname'],
        "lname": request.form['lname'],
        "age": request.form['age'],
    }
    Ninja.create(data)
    return redirect("/dojos")

@app.route("/edit/<int:id>")
def edit_ninja(id):
    data={
        "id":id
    }
    return render_template("/edit.html",ninja=Ninja.get_one(data))

@app.route("/edit/ninja",methods=["POST"])
def edit():
    Ninja.edit(request.form)
    return redirect("/dojos")

@app.route("/delete/<int:id>")
def delete(id):
    data={
        "id":id
    }
    Ninja.delete_ninja(data)
    return redirect("/dojos")