from flask import Flask,render_template,jsonify,request
from models import GenericData
app=Flask(__name__)
#website
@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/genericdata')
def generic_data_page():
    gDList=GenericData.listGenericDataFiles()
    request_url="/static/genericdata"
    return render_template('genericdata.html',gDList=gDList,rUrl=request_url)
#api endpoints
@app.route('/getdata/<genericdata>/<number>')
def getdata(genericdata,number=100):
    data=GenericData.genericDataActions(genericdata,int(number))
    response={}
    if(data!={} and data!=False and data!=None):
        data+=[{"endpoint":"/getdata/{gd}/[number]".format(gd=genericdata)}]
        response=jsonify({data})
    else:
        #run diagnostics on generic data - new thread or process
        #log the error to a file
        response=jsonify({"state":"error","genericdata":{},"message":"There seems to be an error getting generic data {g}".format(g=genericdata)})
    return response

if __name__=="__main__":
    app.run(debug=True)