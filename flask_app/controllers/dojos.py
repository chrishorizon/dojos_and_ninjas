from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def home():
    dojos = Dojo.get_info()
    return render_template('index.html', all_dojos=dojos)

@app.route('/dojos/create', methods=['POST'])
def create():
    Dojo.add_dojo(request.form)
    return redirect('/dojos')

@app.route('/dojo/<int:id>')
def list_dojo(id):
    info = {
        'id':id
    }
    return render_template('dojo.html', dojo=Dojo.get_ninja(info))