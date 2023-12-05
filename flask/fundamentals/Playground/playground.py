from flask import Flask, render_template
app = Flask(__name__)
print(__name__)

# Have the /play route render a template with 3 blue boxes


# level 1
@app.route('/')
def Welcome():
    return render_template("index.html")

# level 3
@app.route("/play/<number>/<color>")
def play(number, color):
    return render_template("index.html", num=int(number), change=color)


# @app.route("/repeat/<number>/<name>")
# def repeat(number, name):
#     str = ""
#     num = int(number)
#     for i in range(num):
#         str += name
#     return str

if __name__ == "__main__":
    app.run(debug=True)


