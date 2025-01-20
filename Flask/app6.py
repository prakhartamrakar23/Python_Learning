from flask import Flask,render_template

app=Flask(__name__)
@app.route('/message')
def msg():
    return render_template('msg.html')

if __name__=="__main__":
    app.run()