from flask_app.config.mysqlconnection import connectToMySQL,DB
from flask import flash
from flask_app.models.user import User

class Recipe:
    def __init__(self,db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.description = db_data['description']
        self.instructions = db_data['instructions']
        self.date= db_data['date']
        self.under_30 = db_data['under_30']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

        self.user_id = None

    # ******Get all******
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes JOIN users ON users.id = recipes.user_id;"
        results = connectToMySQL(DB).query_db(query)
        recipes = []
        if results:
            for row in results:
                recipe = cls(row)
                user_data = {
                    'id': row['users.id'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'email': row['email'],
                    'password': row['password'],
                    'created_at': row['users.created_at'],
                    'updated_at': row['users.updated_at']
                }
                recipe.user = User(user_data)
                recipes.append(recipe)
        return recipes
    
    # ******Get one by id******
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM recipes JOIN users ON users.id = recipes.user_id WHERE recipes.id = %(id)s;"
        results = connectToMySQL(DB).query_db(query , data)

        if results:
            recipe = cls(results[0])
            user_data = {
                'id': results[0]['users.id'],
                'first_name': results[0]['first_name'],
                'last_name': results[0]['last_name'],
                'email': results[0]['email'],
                'password': results[0]['password'],
                'created_at': results[0]['users.created_at'],
                'updated_at': results[0]['users.updated_at']
            }
            recipe.user = User(user_data)
            return recipe
        return False

    # ******Create******
    @classmethod
    def save(cls,data):
        query = "INSERT INTO recipes (name , description , instructions , date , under_30 , user_id) VALUES (%(name)s , %(description)s , %(instructions)s , %(date)s , %(under_30)s , %(user_id)s);"
        return connectToMySQL(DB).query_db(query, data)
    
    
    # ******Update******
    @classmethod
    def update(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date = %(date)s, under_30 = %(under_30)s WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query,data)
    
    # ******Delete******
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query,data)

    # *****Validate_Recipe*****
    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe['name']) < 3:
            is_valid = False
            flash("Name must be at least 3 characters","recipe")
        if len(recipe['instructions']) < 3:
            is_valid = False
            flash("Instructions must be at least 3 characters","recipe")
        if len(recipe['description']) < 3:
            is_valid = False
            flash("Description must be at least 3 characters","recipe")
        if recipe['date_made'] == "":
            is_valid = False
            flash("Please enter a date","recipe")
        return is_valid
