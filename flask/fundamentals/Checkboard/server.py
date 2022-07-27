from flask import Flask, render_template 
app = Flask(__name__)

@app.route('/')
def part_one():
    return render_template("index.html",row=8,col=8,color_one='red',color_two='black')

@app.route('/<int:col>')
def part_two(col):
    return render_template("index.html",col=col,row=8,color_one='red',color_two='black')

@app.route('/<int:col>/<int:row>')
def part_three(col,row):
    return render_template("index.html",col=col,row=row,color_one='red',color_two='black')

@app.route('/<int:col>/<int:row>/<string:color_one>/<string:color_two>')
def sensei_bonus(col,row,color_one,color_two):
    return render_template("index.html",col=col,row=row,color_one=color_one,color_two=color_two)

if __name__=="__main__":    
    app.run(debug=True)