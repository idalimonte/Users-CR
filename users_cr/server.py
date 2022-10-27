from flask import Flask, render_template, request, redirect
from users import User
app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/user')

@app.route('/user')
def read():
    return render_template("read.html", users = User.get_all_users())

@app.route('/user/create')
def create():
    return render_template("create.html")

@app.route('/user/new', methods=['POST'])
def new():
    data = {
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email']
    }
    User.add_user(data)
    return redirect('/user')


@app.route('/user/edit/<int:id>')
def edit(id):
    data = {   
    "id":id 
    }
    return render_template("users_edit.html", user= User.read_one(data))


@app.route('/user/one/<int:id>')
def show_one(id):
    data = {   
    "id":id 
    }
    return render_template("read_one.html", user= User.read_one(data))

@app.route('/user/update', methods=["POST"])
def update():
    User.update(request.form)
    return redirect('/user')

@app.route('/user/delete/<int:id>')
def delete(id):
    data = {
        "id":id
    }
    User.delete(data)
    return redirect('/user')


if __name__ == "__main__":
    app.run(debug=True)
