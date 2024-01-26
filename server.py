from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
app = Flask(__name__,template_folder="static", static_folder="static")

@app.route("/")
def index():
    return "<p>Hello, World!</p>"

@app.route('/contact', methods=['POST', 'GET'])
def contact():
    error = None
    if request.method == 'POST':
        print(request.form)
        # print(request.form["name"])
        # print(request.form["email"])
        # print(request.form["phonenumber"])
        # print(request.form["message"])
        
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return redirect('/static/contact.html')