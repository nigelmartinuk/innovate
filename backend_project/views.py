from flask import render_template, redirect, url_for, request, Blueprint

alias = Blueprint('alias', __name__)

@alias.route("/")    
def home():
    return render_template('index.html')

@alias.route("/home")
def home_redirect():
    return redirect(url_for("alias.home"))

@alias.route("/about")
def about():
    return render_template('about.html')    

@alias.route("/contact")
def contact():
    return render_template('contact.html')
