from flask import Flask
#from flask import abort, jsonify
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

@app.errorhandler(404) 
def invalid_route(e): 
    return "Sorry! No response. Try again."

if __name__=="__main__":    
    app.run(debug=True)