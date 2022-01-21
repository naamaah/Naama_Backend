import requests
from flask import Flask, redirect, render_template, request, session, url_for, jsonify
from interact_with_DB import interact_db

app=Flask(__name__)
app.secret_key = '123'

from Assignment10.Assignment10 import Assignment10
app.register_blueprint(Assignment10)


@app.route('/home')
@app.route('/')
def homeFunc():
    return render_template('index.html')

@app.route('/assignment8')
def assignmentFun ():
    name = 'Naama'
    lastName= 'Aharony'
    uni = "Ben-gurion"
    return render_template('assignment8.html',
                           profile={'name': name, 'lastName': lastName},  # dict
                           university=uni,
                           hobbies=('Gym', 'Kangoo-jump', 'Netflix', 'Movies'),  # tuple
                            currentTV = ['friends', 'X-factor'])



#assignmnet9 functions:
users = {'user1': {'name': 'Yossi', 'email': 'yossi@gmail.com'},
         'user2': {'name': 'Naama', 'email': 'naama10@gmail.com'},
         'user3': {'name': 'Ron', 'email': 'ron1995@gmail.com'},
         'user4': {'name': 'Evia', 'email': 'evia98@gmail.com'},
         'user5': {'name': 'Yotam', 'email': 'yotam29@gmail.com'} }

def checkInput (input):
    for user in users.values():
        if (user['email'] == input or user['name'] == input):
            return (user['email'],  user['name'])
    return False #the input didnt exits in the list or it is empty

@app.route('/assignment9' , methods=['GET','POST'])
def assignment9Func ():
    if request.method == 'GET':
        if 'searchInput' in request.args:
            print (request.args['searchInput'])
            if (checkInput(str(request.args['searchInput'])) != False):
                email = checkInput(request.args['searchInput'])[0]
                name = checkInput(request.args['searchInput'])[1]
                return render_template('assignment9.html', name=name, email=email)
        return render_template('assignment9.html', users=users) #else return all user dict
    if request.method == 'POST':
        nickname=request.form['nickName'] #key name from login page
        session['username'] = nickname
        return render_template("assignment9.html", nickname=nickname, users=users)
    return render_template('assignment9.html', users=users)


@app.route('/logout', methods=['GET','POST'])
def logOutFunc ():
    session['username'] = ''
    return redirect (url_for('assignment9Func'))

##assignment11 functions:
@app.route('/assignment11/users')
def show_users_json():
    query = "select * from users"
    query_result = interact_db(query=query, query_type='fetch')
    return_dict={}
    for user in query_result:
        return_dict[f'user{user.id}'] = {
                       'name': user.Name,
                       'email': user.Email}

    return jsonify(return_dict)


def get_user_By_Id(user_id):
    user = requests.get(f' https://reqres.in/api/users/{user_id}')
    user = user.json()
    return user

@app.route('/assignment11/outer_source', methods=['GET', 'POST'])
def ass11_outer_source():
    if request.method == 'POST':
        user_id = request.form['id']
        user_return = get_user_By_Id(user_id)
        return render_template('assignment11.html', user_return=user_return)
    return render_template('assignment11.html')

@app.route('/assignment12/restapi_users/', defaults={'User_Id': 1})
@app.route('/assignment12/restapi_users/<int:User_Id>', methods=['GET', 'POST'])
def ass12_userID(User_Id):
    query = "select * FROM users WHERE id='%s'" % User_Id
    query_result = interact_db(query=query, query_type='fetch')
    if len(query_result) == 0:
        return_dict = {'status': 'failed', 'message': 'user not found'}
    else:
        return_dict = {'ID': query_result[0].id,
                       'name': query_result[0].Name,
                       'email': query_result[0].Email}
    return jsonify(return_dict)


if __name__ == "__main__":
    app.secret_key = '123'
    app.run(debug=True)