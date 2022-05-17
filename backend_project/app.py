from flask import Flask, render_template, redirect, Blueprint
from views import alias

# create flask website object
app = Flask(__name__)
# attach website views to website object using blueprint created in views.py
app.register_blueprint( alias)

# register a 404 error handler for the website
@app.errorhandler( 404)
def page_not_found(e):
#    return 'This page does not exist', 404
    return render_template("404.html", e=e)

# @app.errorhandler( 404)
# def page_not_found(error):
# #    return 'This page does not exist', 404
#     render_template("404.html", e=error)

# the create flask website object was successful, 
if __name__ == "__main__":
    app.run(debug=True, port=8000) # start the localhost debug webserver
