from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return "Dojo"

@app.route('/say/<name>')
def greeting(name):
    print(name)
    return "Hi " + str(name) + "!"

@app.route('/repeat/<number>/<text>')
def repeat(number,text):
    return str(text) * int(number)

@app.errorhandler(Exception)
def page_not_found():
    return "Sorry! No response. Try again."

if __name__=="__main__":    
    app.run(debug=True)