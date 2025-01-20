#making the routes function name will not be same
from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "Welcome to home page"

@app.route("/about")
def about():
    return "about page"
 
@app.route("/contact")
def contact():
    return "contact page"

if __name__=="__amin__":
    app.run(debug=True)