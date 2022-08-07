from flask import Flask, render_template, redirect, request
from user import User

app= Flask(__name__)


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
    User.create(data) #calling create metho
    return redirect("/")

@app.route("/new")
def new_user():
    return render_template("new.html")



if __name__ == "__main__":
    app.run(debug=True)