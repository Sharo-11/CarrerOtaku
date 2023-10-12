from flask import Flask, render_template

app = Flask(__name__)

# Configure the static folder for CSS and images
app.static_folder = 'static'

@app.route('/')
def first_page():
    return render_template("login.html")

@app.route('/create')
def create_acc():
    return render_template("create.html")

@app.route('/signinascompany')
def signin_company():
    return render_template("signincompany.html")

@app.route('/signinasstudent')
def signin_student():
    return render_template("signinstudent.html")

@app.route('/student')
def student():
    return render_template("student.html")

if __name__ == '__main__':
    app.run(debug=True)