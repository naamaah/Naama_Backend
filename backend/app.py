"""
Assigment7
@app.route('/home')
@app.route('/')
def homeFunc():
    return 'welcome to homePage'

@app.route('/about', methods=['GET', 'POST'])
def aboutFun ():
    return redirect('/') #redirect to homePage

@app.route('/catalog')
def catalog():
    return redirect(url_for(homeFunc))

if __name__ == "__main__":
    app.run(debug=True)

"""
from flask import Flask, redirect, render_template
app=Flask(__name__)

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
                            currentTV = ['friends', 'X-factor'])   #tuple

if __name__ == "__main__":
    app.run(debug=True)