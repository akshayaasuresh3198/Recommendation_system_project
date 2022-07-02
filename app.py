#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask,render_template,request
import pickle
import pandas as pd
import model

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def product_display():
    
    if request.method=='POST':
        user_name=request.form['user_name']
        
        
        output_list=[]
    
        if len(user_name)>0:
            output_list=model.predicttopfive(user_name)
        
        return render_template("index.html",predicted_product=output_list)

    else:
        return render_template("index.html")


if __name__=='__main__':
    app.run(port=5001)
    
    


# In[ ]:




