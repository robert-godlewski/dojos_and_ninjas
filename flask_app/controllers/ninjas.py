from flask_app import app
from flask import render_template, redirect, request
from flask_app.models import dojo, ninja


@app.route('/ninjas')
def new_ninja(): 
    return render_template('new_ninja.html', dojos=dojo.Dojo.get_all())

@app.route('/ninja/create', methods=['POST'])
def create_ninja():
    ninja.Ninja.save(request.form)
    data_id = request.form['dojo_id']
    return redirect(f"/dojos/{data_id}")
