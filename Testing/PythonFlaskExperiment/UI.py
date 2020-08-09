from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, TextField, SubmitField, DateField, IntegerField
from wtforms.validators import DataRequired, Length
from flask import Flask, url_for, render_template, redirect, request, session

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class CustomerForm(FlaskForm):
    """Customer form."""
    name = StringField('Name', [
        DataRequired()])
    dob = StringField('DoB', [
        DataRequired()])
    address = TextField('Address', [
        DataRequired(),
        Length(min=4, message=('Your message is too short.'))])
    noOfChild = StringField('NoOfChildren', [
        DataRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')

class CustomerForm2(FlaskForm):
    """Customer form 2."""
    i = 1
    def __init__(self, i = 1):
         self.i = i
    name = [StringField('Name', [
        DataRequired()])] * i
    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')

@app.route('/')
def home():
    form = CustomerForm()
    return render_template('template.html', form=form)

@app.route('/part1', methods=['GET', 'POST'])
def CustInfo():
    form = CustomerForm()
#    if form.validate_on_submit():
    print(form.name)
    print(form.dob)
    print(form.address)
    print(form.noOfChild)
    session['noOfChild'] = form.noOfChild
#    return redirect(url_for('CustInfo2'))
    return render_template('template2.html', form=form, noOfChild= int(request.form['noOfChild']))

@app.route('/part2', methods=['GET', 'POST'])
def CustInfo2():
    form = CustomerForm2(session['noOfChild'])
#    if form.validate_on_submit():
    for name in form.name:
        print(name)
    return redirect(url_for('success'))
#    return render_template('template2.html', form=form)

@app.route('/success', methods=['POST'])
def success():
    return "Information has been recorded"

if __name__ == "__main__":
    app.run()
