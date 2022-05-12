from flask import render_template, redirect, url_for, request, Blueprint

alias = Blueprint('alias', __name__)

# default route points to our colleague's original javascript page
@alias.route("/")    
def home():
    return render_template('index.html')

# these three routes point to the default index.html page
@alias.route("/javascript")
@alias.route("/js")
@alias.route("/home")
def home_redirect():
    return redirect(url_for("alias.home"))

@alias.route("/about")
def about():
    return render_template('about.html')    

@alias.route("/page1")
def page1():
    return render_template('page1.html')

@alias.route("/page2")
def page2():
    return render_template('page2.html')

@alias.route("/page3")
def page3():
    return render_template('page3.html')

@alias.route("/page4")
def page4():
    return render_template('page4.html')

@alias.route("/page5")
def page5():
    return render_template('page5.html')
