from flask import Flask, render_template,session,redirect,request

app = Flask(__name__)
app.secret_key = "secret key"

@app.route("/")
def index():
    #count defines the session in index.html
    if "count" not in session:
        session["count"] = 0
    else:
        session['count'] += 2
    return render_template("index.html")

@app.route("/destroy_session")
def destroy():
    session.clear()
    return redirect("/")

@app.route("/increment", methods=["POST"])
def increment():
    session['count'] += int(request.form['increment'])
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)