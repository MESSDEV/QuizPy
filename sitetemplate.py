""" The program uses flask and runs a web server. 
When requesting this server, it returns the contents of the index.html file
In this version, it is assumed that there may be a template in the file. """
from flask import Flask, render_template
import os
def index():
    """ the function handles the template index.html and returns the resulting document"""
    return render_template('index.html')


folder = os.getcwd()  # remembering the current working folder
# Creating a web application object:
app = Flask(__name__, template_folder=folder, static_folder=folder) 
# the first parameter is the module name
# the parameter named static_folder defines the name of the folder containing the static files
# the parameter named template_folder defines the name of the folder containing the templates


# creating a rule for URL '/': 
app.add_url_rule('/', 'index', index)


if __name__ == "__main__":
    # Starting the web server:
    app.run()
