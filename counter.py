from flask import Flask, session
def index():
   """ When visiting the site, we reset the counter and provide a link to the page with the counter change """
   session['counter'] = 0
   return '<a href="/counter">Next</a>'
 
def counter():
   """ Increasing the counter and giving a link to the page with the counter change """
   session['counter'] += 1
   return '<h1>' + str(session['counter']) + '</h1>'
# Creating a web application object:
app = Flask(__name__) 
app.config['SECRET_KEY'] = 'VeryStrongKey'
app.add_url_rule('/', 'index', index) # creates a rule for the URL '/':
                       # run the index function and return its value.
app.add_url_rule('/counter', 'counter', counter) # creates a rule for the URL 'counter/'
 
if __name__ == '__main__':
   # Starting the web server:
   app.run()
