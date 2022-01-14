from flask import redirect, render_template, request, Blueprint, jsonify
from interact_with_DB import interact_db

# Assignment10 blueprint definition
Assignment10 = Blueprint('Assignment10', __name__,
                        static_folder='static',
                        static_url_path='/Assignment10',
                        template_folder='templates')

@Assignment10.route('/Assignment10' , methods=['GET','POST'])
def assignment10Func ():
    query = "select * from users"
    query_result = interact_db(query=query, query_type='fetch')
    return render_template("Assignment10.html", users=query_result)

@Assignment10.route('/insert_user', methods=['POST'])
def insert_user_func():
    name=request.form['name']
    email = request.form['email']
    query="INSERT INTO users (name, email) VALUES ('%s', '%s')" % (name, email)
    interact_db(query, query_type='commit')
    return redirect('/Assignment10')

@Assignment10.route('/update_user', methods=['POST'])
def update_user_func():
    name=request.form['name']
    email = request.form['email']
    query = "UPDATE users SET Name = '%s' WHERE Email='%s';" % (name, email)

    interact_db(query, query_type='commit')
    return redirect('/Assignment10')

@Assignment10.route('/delete_user', methods=['POST'])
def delete_user_func():
    email=request.form['email']
    query= "DELETE FROM users WHERE email='%s'" % email
    interact_db(query, query_type='commit')
    return redirect('/Assignment10')


