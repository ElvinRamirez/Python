from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

NAME_REGEX = re.compile(r'^[a-zA-Z]')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
PASSWORD_REGEX = re.compile(r'^(?=.{8,}$)(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*\W).*$')

class User:
    db = 'users_schema'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def create(cls,data):
        query = "INSERT INTO users (first_name,last_name, email, password, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(email)s, %(password)s,NOW(), NOW());"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        user = connectToMySQL(cls.db).query_db(query,data)
        if len(user) < 1:
            return False
        return cls(user[0])

    @classmethod    
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        return cls(results[0])

    @staticmethod
    def validate_user(user):
        is_valid = True 
        query = 'SELECT * FROM users WHERE email = %(email)s;'
        results = connectToMySQL(User.db).query_db(query,user)
        if len(results) >= 1:
            flash("Email already taken.","register")
            is_valid=False
        if len(user['fname']) < 2:
            flash("Name must be at least 2 characters.","register")
            is_valid = False
        if not NAME_REGEX.match(user['fname']): 
            flash("Invalid first name!","register")
            is_valid = False
        if len(user['lname']) < 2:
            flash("Name must be at least 2 characters.","register")
            is_valid = False
        if not NAME_REGEX.match(user['lname']): 
            flash("Invalid last name!","register")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!","register")
            is_valid = False
        if not PASSWORD_REGEX.match(user['password']):
            flash("Password must have at least 1 number and 1 uppercase letter","register")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters.","register")
            is_valid = False
        if user['password'] != user['cpassword']:
            flash("Passwords don't match","register")
            is_valid = False
        return is_valid