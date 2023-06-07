from flask import Flask
from flask import request
from flask import render_template
import json

app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def about():


    return render_template('about.html')

@app.route('/macro')
def macro():

    f = open("data/csvjson.json", "r")
    data = json.load(f)
    f.close()

    for point in data:
        print(point["Year"])
        print(point['Month'])

    return render_template('macro.html')

@app.route('/micro')
def micro():
    
    return render_template('micro.html')

app.run(debug=True)
