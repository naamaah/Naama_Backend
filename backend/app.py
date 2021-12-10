# include - instead of copy paste we use something more modolary

from flask import Flask, redirect, url_for
app=Flask(__name__)

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