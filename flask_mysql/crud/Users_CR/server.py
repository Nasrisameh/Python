from flask import Flask, render_template, request, redirect
# import the class from user.py
from users import User
app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    return render_template("users.html" , users=User.get_all)

@app.route('/users/new')
def new():
    return render_template("create.html")

# @app.route('/create_user' , methods=["POST"])
# def create_user():
#     data = {
#         "fname": request.form["fname"],
#         "lname": request.form["lname"],
#         "email": request.form["email"]
#     }
#     # We pass the data dictionary into the save method from the User class.
#     User.save(data)
#     # Don't forget to redirect after savig to the database.
#     return redirect('/users')

@app.route('/users/create',methods=['POST'])
def create():
    User.save(request.form)
    return redirect('/users')


if __name__ == "__main__":
    app.run(debug=True)