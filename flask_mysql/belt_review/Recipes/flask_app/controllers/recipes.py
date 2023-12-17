from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe


# *****CREATE*****
# route :/create/recipe
@app.route('/create/recipe',methods=['POST'])
def create_recipe():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes/new')
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "under_30": int(request.form["under_30"]),
        "date": request.form["date"],
        "user_id": session["user_id"]
    }
    Recipe.save(data)
    return redirect('/dashboard')

# *****NEW RECIPE*****
# route 8:/recipe/new
@app.route('/recipes/new')
def new_recipe():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('one_recipe.html', user = User.get_by_id(data))

# *****UPDATE*****
# route :/edit/recipe/{{recipe.id}}
@app.route('/edit/recipe/<int:id>')
def edit_recipe(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("edit_recipe.html", edit = Recipe.get_one(data), user = User.get_by_id(user_data))

# route :/update/recipe
@app.route('/update/recipe',methods=['POST'])
def update_recipe():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Recipe.validate_recipe(request.form):
        return redirect('/new/recipe')
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "under_30": int(request.form["under_30"]),
        "date": request.form["date"],
        "id": request.form['id']
    }
    Recipe.update(data)
    return redirect('/dashboard')

# *****SHOW*****
# route :/recipe/{{recipe.id}}
@app.route('/recipe/<int:id>')
def one_recipe(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("one_recipe.html", recipe = Recipe.get_one(data), user = User.get_by_id(user_data))

# route :destory/recipe/{{recipe.id}}
@app.route('/destroy/recipe/<int:id>')
def destroy_recipe(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Recipe.destroy(data)
    return redirect('/dashboard')