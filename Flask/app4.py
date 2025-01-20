# we can add the url to any route using this add_url_rule()

from flask import Flask
app=Flask(__name__)

def home():
    return "<h1>HOME Page</h1>"

#add_url_rule(<url rule>, <endpoint>, <view function>)  it takes three urls
app.add_url_rule("/home","home",home)

if __name__=="__main__":
  app.run(debug=True)