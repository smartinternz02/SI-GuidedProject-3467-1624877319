import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from monkeylearn import MonkeyLearn
import os 

app = Flask(__name__)
x = pickle.load(open('keywords extraction.ipynb','r'))

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/extraction',methods=['POST'])
def extraction():
    p = request.form['a ']
    print(p)
    return render_template('keywordextractionapii.py')

if __name__ == "__main__":
    app.run(debug=True)