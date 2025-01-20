from flask import Flask,request

app=Flask(__name__)
@app.route('/login',methods=["POST"])
def login():
    uname=request.form['uname']
    passward=request.form['pass']
    if uname=='prakhar' and passward=="google":
        return "Welcome",uname
    
if __name__ == '__main__':  
   app.run(debug = True)    