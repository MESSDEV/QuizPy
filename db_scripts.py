from random import randint
from flask import Flask, session, redirect, url_for
from db_scripts import get_question_after
quiz = 0
last_question = 0
def index():
   global quiz, last_question
   max_quiz = 3
   # or if the student wrote get_quiz_count(), then you can import it and specify:
   # max_quiz = get_quiz_count[0] 
   quiz = randint(1, max_quiz)
   # or if the student wrote get_quiz_count(), then you can import it and specify:
   # session['quiz'] = get_random_quiz_id()
   last_question = 0
   return '<a href="/test">Test</a>'
def test():
   global last_question
   result = get_question_after(last_question, quiz)
   if result is None or len(result) == 0:   
           return redirect(url_for('result'))
 
   else:
       last_question = result[0]
       # if we've taught the database to return Row or dict, then we shouldn't write result[0] and instead write result['id']
       return '<h1>' + str(quiz) + '<br>' + str(result) + '</h1>'
def result():
   return "that's all folks!"
# Creating a web application object:
app = Flask(__name__)  
app.add_url_rule('/', 'index', index) # creates a rule for the URL '/'
app.add_url_rule('/test', 'test', test) # creates a rule for the URL '/test'
app.add_url_rule('/result', 'result', result) # creates a rule for the URL '/test'
if __name__ == '__main__':
   # Starting the web server:
   app.run()
