from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app) 

@app.route('/user/<name>')
def index(name):
   #hardcoded method
   #return '<h1>Hello World!</h1>'

   #Now adding datetime variable
   name=name
   return render_template('user.html',current_time=datetime.utcnow(),name=name)
   

#@app.route('/user/<name>')
#def user(name):
  # hardcoded method
  # return '<h1>Hello, %s!</h1>' % name

  # Now adding Bootstrap
 # return render_template('user.html',name=name)


if __name__ == '__main__':
   app.run(debug=True)
