import os
import numpy as np
from flask import Flask,request,render_template
from keras.models import load_model
import tensorflow as tf
from PIL import Image

app=Flask(__name__)
model=load_model('ECG.h5')

@app.route("/") 
def about():
    return render_template("home.html")

@app.route("/home") 
def home():
    return render_template("home.html")

@app.route("/info") 
def info():
    return render_template("info.html")

@app.route("/guide") 
def guide():
    return render_template("guide.html")

@app.route("/predict") 
def test():
    return render_template("predict.html")

@app.route("/predict",methods=["GET","POST"]) 
def upload():
    if request.method=='POST':
        f=request.files['file'] 
        basepath=os.path.dirname('__file__')
        filepath=os.path.join(basepath,"uploads",f.filename)
        f.save(filepath)
        
        img=tf.keras.utils.load_img(filepath,target_size=(128,128))
        x=tf.keras.utils.img_to_array(img)
        x=np.expand_dims(x,axis=0)
        
        pred=model.predict(x)
        y_pred = np.argmax(pred)
        print("prediction",y_pred)
    
        index=['Left Bundle Branch Block','Normal','Premature Atrial Contraction',
       'Premature Ventricular Contractions', 'Right Bundle Branch Block','Ventricular Fibrillation']
        result=str(index[y_pred])

        return result
    return None

if __name__=="__main__":
    app.run(debug=False)          