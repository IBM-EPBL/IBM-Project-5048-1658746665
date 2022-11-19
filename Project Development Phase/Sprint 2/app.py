import os
import numpy as np
from flask import Flask,request,render_template
from keras.models import load_model
import tensorflow as tf
from PIL import Image

app=Flask(__name__)

@app.route("/") 
def about():
    return render_template("home.html")

@app.route("/home") 
def home():
    return render_template("home.html")

@app.route("/info") 
def information():
    return render_template("info.html")

@app.route("/guide") 
def information():
    return render_template("guide.html")

@app.route("/predict") 
def test():
    return render_template("predict.html")

if __name__=="__main__":
    app.run(debug=False)          