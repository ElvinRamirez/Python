from flask import Flask, render_template,session,redirect,request


app = Flask(__name__)
app.secret_key = "Secrecy"

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    session['student'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('result')

@app.route("/result")
def result():
    return render_template("result.html",student=session['student'])
    
if __name__ == "__main__":
    app.run(debug=True)