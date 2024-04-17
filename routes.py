from flask import render_template, url_for, request, redirect, Flask, flash, session
import os
from flask_login import UserMixin, login_required, login_user, LoginManager, logout_user, current_user
from werkzeug.utils import secure_filename
from extensions import *

def setup_routes(app: Flask):
    @app.route('/')
    def first_page():
        return render_template("login.html")

    @app.route('/create')
    def create_acc():
        return render_template("create.html")

    @app.route('/student')
    def student():
        return render_template("student.html")
    
    @app.route('/student/<int:student_id>')
    @login_required
    def student_profile(student_id):
        student = Student.query.get_or_404(student_id)
        return render_template("student.html", student=student)
