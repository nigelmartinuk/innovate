from flask import Flask, render_template, redirect, Blueprint
from views import alias

app = Flask(__name__) 

app.register_blueprint( alias)

if __name__=="__main__":
    app.run(debug=True, port=8000)
