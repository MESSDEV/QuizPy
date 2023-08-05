from random import randint
from flask import Flask, session, redirect, url_for
from db_scripts import get_question_after
def index():
   max_quiz = 3
   # or if the student wrote get_quiz_count(), then you can import it and specify:
   # max_quiz = get_quiz_count[0] 
   session['quiz'] = randint(1, max_quiz)
   # or if the student wrote get_quiz_count(), then you can import it and specify:
   # session['quiz'] = get_random_quiz_id()
   session['last_question'] = 0
   return '<a href="/test">Test</a>'
​
def test():
   result = get_question_after(session['last_question'], session['quiz'])
   if result is None or len(result) == 0:
       return redirect(url_for('result'))
   else:
       session['last_question'] = result[0]
       # if we've taught the database to return Row or dict, then we shouldn't write result[0] and instead write result['id']
       return '<h1>' + str(session['quiz']) + '<br>' + str(result) + '</h1>'
​
def result():
   return "that's all folks!"
​
# Creating a web application object:
app = Flask(__name__) 
app.add_url_rule('/', 'index', index) # creates a rule for the URL '/'
app.add_url_rule('/test', 'test', test) # creates a rule for the URL '/test'
app.add_url_rule('/result', 'result', result) # creates a rule for the URL '/test'
# Setting the encryption key:
app.config['SECRET_KEY'] = 'ThisIsSecretSecretSecretLife'
​
if __name__ == '__main__':
   # Starting the web server:
   app.run()
