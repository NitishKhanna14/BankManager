from application import app # ,db
from flask import render_template, request, json, Response, redirect, flash, url_for

nav_details={
    'login' : False
}


@app.route("/", methods=['GET','POST'])
def func_main():
    global nav_details
    

    if(nav_details['login']==True):
        return render_template("index.html",nav=nav_details)

    else:
        return redirect("/login")

@app.route('/login', methods=['GET','POST'])
def func_login():
    global nav_details

    if(nav_details['login']==True):
        return redirect("index.html",nav=nav_details) 
        #if login is true this means the word "logout" was showing to user
        # which he/she clicked redirect to index with a post request to
        #  logout the user 

    else : 
        return render_template("login.html",nav=nav_details)
