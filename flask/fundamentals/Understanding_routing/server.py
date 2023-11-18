from flask import Flask ,render_template
app = Flask(__name__)
# localhost:5000/ - have it say "Hello World!"
@app.route('/')
def hello_world():
    return 'Hello World!'

# localhost:5000/dojo - have it say "Dojo!"
@app.route('/dojo')
def dojo():
    return "Dojo"

# Create one url pattern and function that can handle the following examples:
# localhost:5000/say/flask - have it say "Hi Flask!"
@app.route('/say/<name>')
def say_name(name):
    return f"Hi {name.capitalize()}!"

# # localhost:5000/say/michael - have it say "Hi Michael!"
@app.route('/say/<name>')
def hi(name):
    print(name)
    return "Hi. " + "Michael"

# Create one url pattern and function that can handle the following examples localhost:5000/say/john 
# - have it say "Hi John!"
@app.route('/say/<string:name>/')
def hi2(name):
    return f"Hi {name}!"

# Create a route that responds with the given word repeated as many times as specified in the URL
# For example, if you go to http://localhost:5000/repeat/35/hello
# It should return "hello hello hello hello..."
@app.route("/repeat/<int:count>/<string:word>")
def repeat(count, word):
    result = ""
    for i in range(0,count):
        result += f"<p>{word}</p>"
    return result

# NINJA BONUS: Ensure the names provided in the 3rd task are strings
# If not, convert them into strings before returning the response
@app.route("/ninja-bonus/<var1>/<var2>/<var3>")
def ninja_bonus(var1, var2, var3):
    # Convert all variables to string type
    strVar1 = str(var1)
    strVar2 = str(var2)
    strVar3 = str(var3)
    # Concatenate all three variables together
    concatenatedString = strVar1 + strVar2 + strVar3
    # Return the concatenated string
    return concatenatedString


# SENSEI BONUS: Ensure that if the user types in any route other than the ones specified, 
# they receive an error message saying "Sorry! No response. Try again."
@app.errorhandler(404)
def page_not_found(e):
    return render_template('page_not_found.html'), 404




if __name__=="__main__":
    app.run(debug=True)
