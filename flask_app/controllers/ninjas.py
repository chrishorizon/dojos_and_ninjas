from flask import render_template, redirect,request
from flask_app import app
from flask_app.models import dojo, ninja

@app.route('/ninjas')
def ninja_list():
    return render_template('ninja.html', dojos = dojo.Dojo.get_info())

@app.route('/create/ninja', methods=['POST'])
def save_ninja():
    ninja.Ninja.add_ninja(request.form)
    return redirect('/dojos')