from flask import Flask,render_template,jsonify,request
from models import GenericData
app=Flask(__name__)
#website
@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/genericdata')
def generic_data_page():
    return render_template('genericdata.html')

@app.route('/mydb/<action>')
def mydb(action):
    return render_template("mydb.html")

#api endpoints
@app.route('/getdata/<genericdata>/<number>')
def getdata(genericdata,number=100):
    data=GenericData.genericDataActions(genericdata,int(number))
    response={}
    if(data!={} and data!=False and data!=None):
        response=jsonify({data,"endpoint":"/getdata/{gd}/[number]".format(gd=genericdata)})
    else:
        #run diagnostics on generic data - new thread or process
        #log the error to a file
        response=jsonify({"state":"error","genericdata":{},"message":"There seems to be an error getting generic data {g}".format(g=genericdata)})
    return response

#fake bank
"""
@app.route('/fakebank')
def fakebankIndex():
    return 
@app.route('/fakebank/pay',[POST])
def pay():
    return 
"""



"""
future features
#mydb
    --create a json file and customize the populated data
    --protect file with key
"""

if __name__=="__main__":
    app.run(debug=True)