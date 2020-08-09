from flask import Flask, render_template, flash, request, session, redirect, url_for
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    address = TextField('Address:', validators=[validators.required(), validators.Length(min=6, max=120)])
    dob = TextField('Dob:', validators=[validators.required(), validators.Length(min=3, max=35)])

    @app.route("/")
    def home():
        return render_template('Template.html') #{{ form.csrf }}

    @app.route("/custdata", methods=['GET', 'POST'])
    def CustForm():
        form = ReusableForm(request.form)

        print(form.errors)
        if request.method == 'POST':
            name=request.form['name']
            address=request.form['address']
            dob=request.form['dob']
            gender=request.form['gender']
            religion=request.form['religion']
            if religion == "muslim":
                flash("Please get lost #CAA!!!")
                return redirect(url_for('home'))
            userInfo = request.form
            for i in userInfo:
                print(userInfo[i])
            session['userInfo'] = userInfo

        if form.validate():
        # Save the comment here.
            flash('Details recorded and processing ')
        else:
            flash('Error: All the form fields are required. ')

        return render_template('Display.html', userInfo=session['userInfo'])

    @app.route("/next", methods=['POST'])
    def GetNext():
        return render_template('TemplateP2.html', userInfo= int(session['userInfo']['noOfChild']))

    @app.route("/custdata2", methods=['GET', 'POST'])
    def CustForm2():
        form = ReusableForm(request.form)

        print(form.errors)
        userInfo = request.form
        for i in userInfo:
            print(userInfo[i])
        session['userInfo'] = userInfo

        if form.validate():
        # Save the comment here.
            flash('Details recorded and processing ')
        else:
            flash('Error: All the form fields are required. ')

        return render_template('Display.html', userInfo=session['userInfo'])


if __name__ == "__main__":
    app.run()
