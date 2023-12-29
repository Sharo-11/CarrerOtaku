from flask import Flask, render_template, redirect, request, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, HiddenField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = "123456787"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'

db = SQLAlchemy(app)

class Students(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    first_name= db.Column(db.String(200),nullable=False)
    last_name= db.Column(db.String(200),nullable=False)
    email= db.Column(db.String(50),nullable=False,unique=True)
    password= db.Column(db.String(50),nullable=False)
    campus= db.Column(db.String(50),nullable=False)
    dept= db.Column(db.String(100),nullable=False )
    date_added=db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self):
        return'<Name %r>' % self.first_name


class StudentForm(FlaskForm):
    first_name = StringField("First Name", validators = [DataRequired()])
    last_name = StringField("Last Name", validators = [DataRequired()])
    email = EmailField("Email", validators = [DataRequired()])
    password = HiddenField("Password", validators = [DataRequired()])
    campus = StringField("Campus", validators = [DataRequired()])
    dept = StringField("Department", validators = [DataRequired()])
    student_id = StringField("Student_id", validators = [DataRequired()])
    submit = SubmitField("Submit")


# Configure the static folder for CSS and images
app.static_folder = 'static'

@app.route('/')
def first_page():
    return render_template("login.html")

@app.route('/create')
def create_acc():
    return render_template("create.html")

@app.route('/signinascompany', methods = ["GET", "POST"])
def signin_company():
    return render_template("signincompany.html")

@app.route('/signinasstudent', methods=["GET", "POST"])
def signin_student():
    first_name = None
    last_name = None
    email = None
    password = None
    campus = None
    dept = None
    student_id = None

    form = StudentForm()
    if request.method == 'POST':
        if form.validate():
            first_name = form.first_name.data
            last_name = form.last_name.data
            email = form.email.data
            password = form.password.data
            campus = form.campus.data
            dept = form.dept.data
            student_id = form.student_id.data

            # Create a User object and add it to the database (assuming you have set up SQLAlchemy)
            user = StudentForm(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
                campus=campus,
                department=dept,
                student_id=student_id
            )

            db.session.add(user)
            db.session.commit()

            # Clear the form data
            form.first_name.data = ""
            form.last_name.data = ""
            form.email.data = ""
            form.password.data = ""
            form.campus.data = ""
            form.dept.data = ""
            form.student_id.data = ""

    return render_template("signinstudent.html",
                           first_name=first_name,
                           last_name=last_name,
                           email=email,
                           password=password,
                           campus=campus,
                           dept=dept,
                           student_id=student_id,
                           form=form)
    
@app.route('/student')
def student():
    return render_template("student.html")

if __name__ == '__main__':
    app.run(debug=True)