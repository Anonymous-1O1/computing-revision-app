from flask import Flask,render_template
import json
from random import randint
with open("def.json","r") as thefile:
    data_json=thefile.read()
defenitions=json.loads(data_json)
object=list(defenitions.keys())

app=Flask(__name__)

@app.route('/')
def root():
    x=randint(0,len(object))
    return render_template('index.html',item=object[x],description=defenitions[object[x]])

if __name__ =="__main__":
    app.run(host="0.0.0.0",port=132)