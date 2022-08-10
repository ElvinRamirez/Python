from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.user import User

@app.route("/")
def index():
    users = User.get_all()
    #print(users)
    return render_template("index.html", users = users) #users = User.get_all also works

@app.route("/create", methods=["POST"])
def create_user():
    data = {
        "fname": request.form['fname'],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }
    User.create(data) #calling create method
    return redirect("/")

@app.route("/new")
def new_user():
    return render_template("new.html")

@app.route("/readone/<int:id>")
def show_one(id):
    data={
        "id":id
    }
    return render_template("/readone.html", user=User.get_one(data))

@app.route("/edit/<int:id>")
def edit_user(id):
    data={
        "id":id
    }
    return render_template("/edit.html",user=User.get_one(data))

@app.route("/edit/user",methods=["POST"])
def edit():
    User.edit(request.form)
    return redirect("/")

@app.route("/delete/<int:id>")
def delete(id):
    data={
        "id":id
    }
    User.delete_user(data)
    return redirect("/")