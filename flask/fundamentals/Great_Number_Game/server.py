from flask import Flask, render_template,session,redirect,request
import random

app = Flask(__name__)
app.secret_key = "Speak friend and enter"

@app.route("/")
def index():
    if "random" not in session:
        session["random"] = random.randint(1,100)
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def user_entry():
    session['entry'] = int(request.form['entry'])
    #need to be able to keep the same random number/session until the user gets it correctly
    #if int(request.form['entry']) != session['random']:
        #print("failed")
    #else:
        #print('hello')
        #session.clear()        
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)