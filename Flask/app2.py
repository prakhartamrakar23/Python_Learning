#using the redirect and url_for to redirect the user to some page

from flask import Flask,redirect,url_for

app=Flask(__name__)

@app.route("/home")
def home():
    return "welcome to home page"
@app.route("/about/")
def about():
    return "welcome to about page"

@app.route("/contact")
def contact():
    return "welcome to contact page"
@app.route("/info/<enquiry>")
def info(enquiry):
    enquiry=""
    if enquiry=="yes":
        return redirect(url_for(about))
    else:
        return redirect(url_for(home))

if __name__=="__main__":
    app.run(debug=True)