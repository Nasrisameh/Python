# import flask
from flask import Flask, render_template
app = Flask(__name__)

# Your program should have the following output
# http://localhost:5000 - should display 8 by 8 checkerboard
@app.route('/')
def index():
    return render_template("index.html",row=8,col=8,color1='red',color2='black')

# Your program should have the following output
# http://localhost:5000/4 - should display 8 by 4 checkerboard
@app.route('/<int:x>')
def row(x):
    return render_template("index.html", row=x, col=8, color1='red', color2='black')

# Your program should have the following output
# http://localhost:5000/(x)/(y) - should display x by y checkerboard.  
# For example, http://localhost:5000/10/10 should display 10 by 10 checkerboard.  
# Before you pass x or y to Jinja, 
# please remember to convert it to integer first (so that you can use x or y in a for loop)
@app.route('/<int:x>/<int:y>')
def board(x, y):
    return render_template('index.html', row=x, col=y, color1='red', color2='black')
# Have another route accept 2 parameters (i.e. "/<x>/<y>") and render a checkerboard with x rows and y columns, 
# with alternating colors
@app.route('/alt/<int:x>/<int:y>')
def alt_board(x, y):
    return render_template('index.html', row=x, col=y, color1='blue', color2='green')
# Have another route accept 4 parameters (i.e. "/<x>/<y>/<color1>/<color2>") and render a checkerboard with x rows and y columns, 
# with alternating colors, color1 and color2
@app.route('/alt-colors/<int:x>/<int:y>')
def alt_colors_board(x, y):
    return render_template('index.html', row=x, col=y, color1='pink', color2='white')
# change 1er color
@app.route('/<int:x>/<int:y>/<string:one>')
def row_col_one(x,y,one):
    return render_template("index.html",row=x,col=y,color1=one,color2='black')
# change 2 colors
@app.route('/<int:x>/<int:y>/<string:one>/<string:two>')
def row_col_two(x,y,one,two):
    return render_template("index.html",row=x,col=y,color1=one,color2=two)

if __name__=="__main__":
    app.run(debug=True)