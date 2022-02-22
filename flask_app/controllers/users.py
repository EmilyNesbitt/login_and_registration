from flask_app import app
from flask_app.models import user
from flask import render_template, redirect,  session, request
from flask_bcrypt import Bcrypt

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/dash')
def dash():
    users = user.User.get_all()
   # print(users)
   #15-26 need to be in a login method
    data = {
        "email":request.form['email'],
        "password":request.form['password'],
        "id":id
    }
    user_in_database = user.User.get_by_email(data)
    if user_in_database == False:
        flash("User not recognized, please register above")
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_database.password, request.form['password']):
        flash("Invalid Email/Password", 'email')
        return redirect('/')
    session['user_id'] = user_in_database.id
    return render_template("Read(all).html", all_users = users)
@app.route('/create')
def index2():
    return render_template("Create.html")

@app.route('/makeuser', methods=['POST'])
def makeuser():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "username": request.form["username"],
        "password": request.form["password"],
        "email" : request.form["email"]
    }
    if not bcrypt.check_password_hash(user_in_database.password, request.form['password']):
        flash("Invalid Email/Password", 'email')
        return redirect('/')
    session['user_id'] = user_in_database.id
    user.User.save(data)
    return redirect('/dash')
@app.route('/updateuser/<int:id>', methods=['POST'])
def updateuser(id):
    data ={
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "username": request.form["username"],
        "password": request.form["password"],
        "email" : request.form["email"],
        "id" : id
    }
    user.User.update(data)
    return redirect('/dash')

@app.route('/show/<int:id>')
def showuser(id):
    data ={
        'id': id
    }
    return render_template(("read(one).html"),user=user.User.get_one(data))
@app.route('/edit/<int:id>')
def edituser(id):
    data ={
        'id': id
    }
    return render_template(("edit.html"),user=user.User.get_one(data))

@app.route('/delete/<int:id>')
def deleteuser(id):
    data ={
        'id': id
    }
    user.User.delete(data)
    return redirect('/dash') 