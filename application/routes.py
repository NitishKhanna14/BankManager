from application import app # ,db
from flask import render_template, request, json, Response, redirect, flash, url_for

nav_details={
    'login' : "abcdef"
}


@app.route("/")
def func_main():
    global nav_details
    return render_template("index.html", nav=nav_details)


@app.route('/login',methods=['GET','POST'])
def func_login():
    return render_template("login.html",nav=nav_details)



@app.route('/logout',methods=['POST'])
def func_logout():
    global nav_details
    nav_details['login']=""
    return redirect('/')

