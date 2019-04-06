from app import app
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, NewPatientForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Patient
from werkzeug.urls import url_parse
from app.forms import RegistrationForm
from app import db


@app.route('/index')
@login_required
def index():
    return render_template('index.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(employee_id=form.employee_id.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid employee id or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(employee_id=form.employee_id.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration Successful!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/employee/<employee_id>',  methods=["GET", "POST"])
@login_required
def employee(employee_id):
    employee = User.query.filter_by(employee_id=employee_id).first_or_404()
    patientform = NewPatientForm()
    if patientform.validate_on_submit():
        patient = Patient(name=patientform.name.data,
                          age=patientform.age.data,
                          gender=patientform.gender.data,
                          height=patientform.height.data,
                          weight=patientform.weight.data,
                          prescription=patientform.prescription.data,
                          medications=patientform.medications.data,
                          tests=patientform.tests.data
                          )
        db.session.add(patient)
        db.session.commit()
        flash('Successfully Added New Patient')
    else:
        flash("Registration Unsuccessful. Kindly input correct form values")
    return render_template('employee_dashboard.html', user=employee, patientform=patientform)
