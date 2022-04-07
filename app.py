#!/usr/bin/env python
# coding: utf-8

# In[46]:


from flask import Flask


# In[47]:


app = Flask(__name__)


# In[48]:


from flask import render_template, request
import joblib

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        email = request.form.get("email")
        web = request.form.get("web")
        print(email, web)
        email = float(email)
        web = float(web)
        model = joblib.load('cybersecurity_model')
        pred = model.predict([[email, web]])
        return(render_template("index.html", result="1"))
    else:
        return(render_template("index.html", result="2"))


# In[49]:


if __name__ == "__main__":
    app.run()


# In[ ]:





# In[ ]:




