from flask import Flask


app=Flask(__name__) # it is entry point of our application

@app.route('/')
def home():
    return "home page"

if __name__=="__main__":
    app.run()