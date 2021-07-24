import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

import os 

app = Flask(__name__)
x = pickle.load(open('F:\keywords ext\keywords extraction.ipynb', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/extraction',methods=['POST'])
def extraction():
    p = request.form['a ']
    print(p)
    return render_template('extraction.html')

if __name__ == "__main__":
    app.run(debug=True)