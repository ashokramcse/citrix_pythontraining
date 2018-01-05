'''
Created on 18-Jul-2017

@author: BALASUBRAMANIAM
'''
from flask import Flask

app = Flask(__name__)

@app.route('/home')
def welcome():
    return 'Welcome to Flask'

if __name__ == '__main__':
    app.run( 
        host="127.0.0.1",
        port=int("5000")
  )