from flask_app import app
from flask_app.models import user
from flask import render_template, redirect,  session, request


@app.route('/')
def index():
    users = user.User.get_all()
    print(users)
    return render_template("Read(all).html", all_users = users)
@app.route('/create')
def index2():
    return render_template("Create.html")

@app.route('/makeuser', methods=['POST'])
def makeuser():
    data = {
        "full_name": request.form["full_name"],
        "email" : request.form["email"]
    }
    user.User.save(data)
    return redirect('/')
@app.route('/updateuser/<int:id>', methods=['POST'])
def updateuser(id):
    data ={
        "full_name": request.form["full_name"],
        "email" : request.form["email"],
        "id" : id
    }
    user.User.update(data)
    return redirect('/')

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
    return redirect('/') 