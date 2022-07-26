from flask import Flask, render_template  # Import Flask to allow us to create our app, this is needed on every flask app**
app = Flask(__name__)    # Create a new instance of the Flask class called "app", also always needed**
@app.route('/')          # The "@" decorator associates this route with the function immediately following
#line 3 is directly associated with the function on line 5
def index():
    return render_template("index.html", phrase="hello", times=5) # Return the string 'Hello World!' as a response

@app.route('/success')
def success():
    return "success"

@app.route('/hello/<string:banana>/<int:num>')
def hello(banana,num):
    return render_template("hello.html",banana= banana,num= num)

@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

if __name__=="__main__":    
    app.run(debug=True)