from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def about():
    #load a current view of the data
    #render the template with the apporpriate data
    return render_template('about.html')

@app.route('/macro')
def macro():

    return render_template('macro.html')

@app.route('/micro')
def micro():
    
    return render_template('micro.html')

app.run(debug=True)
