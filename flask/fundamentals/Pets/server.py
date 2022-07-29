from flask import Flask, render_template, session,redirect,request  
app = Flask(__name__)
from data import trainingSchool
app.secret_key = "Josh is the man today"

@app.route('/')
def index():
    if 'user' not in session:
        return render_template('logReg.html')
    else:
        return render_template('index.html, cohorts=trainingSchool')

#This is a hidden route
@app.route('/createUser', method=['post'])
def createUSer():
    session['user'] = request.form['fullName']
    return redirect('/')

@app.route('/cohort/<int:cohort_id>/view')
def viewCohort(cohort_id):
    if 'user' not in session:
        return render_template('logReg.html')
    else:
        return render_template('index.html, cohorts=trainingSchool')

if __name__=="__main__":    
    app.run(debug=True)