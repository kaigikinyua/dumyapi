import flask
from flask import Flask,render_template,jsonify,request
from models import GenericData
from utils import JsonFile
from customJson import *
app=Flask(__name__)
#website
@app.route('/')
def index():
    return render_template("index.html")

#generic data webpage
@app.route('/genericdata')
def generic_data_page():
    gDList=GenericData.listGenericDataFiles()
    request_url="/static/genericdata"
    return render_template('genericdata.html',gDList=gDList,rUrl=request_url)

#generated data overview
@app.route('/ddl',methods=["GET","POST"])
def generated_data_page():
    print(request.environ.get('HTTP_ORIGIN','*'))
    if(request.method=="POST"):
        data=request.get_json("body")
        c=CustomJson(str(data))
        res=c.populateJson()
        response=flask.make_response(jsonify({"result":res}))
        response.headers.add('Access-Control-Allow-Origin','*')
        response.headers.add('Access-Control-Allow-Headers','Content-Type,Authorization')
        print(response)
        return response
    else:
        ddl_variables=JsonFile.loadData("./variables.json")
        return render_template('generated_data.html',ddl_variables=ddl_variables["variables"])

#generic data endpoint
@app.route('/getgenericdatacache/<genericdata>/<number>')
def getdata(genericdata,number=100):
    data=GenericData.genericDataActions(genericdata,int(number))
    response_data={}
    print(data)
    if(data!={} and data!=False and data!=None):
        #data+=[{"endpoint":"/getgenericdatacache/{gd}/[number]".format(gd=genericdata)}]
        response_data=jsonify(data)
    else:
        #run diagnostics on generic data - new thread or process
        #log the error to a file
        response_data=jsonify({"state":"error","genericdata":{},"message":"There seems to be an error getting generic data {g}".format(g=genericdata)})
    response=flask.make_response(response_data)
    response.headers.add('Access-Control-Allow-Origin','*')
    response.headers.add('Access-Control-Allow-Headers','Content-Type,Authorization')
    print(request.environ.get('HTTP_ORIGIN','default_value'))
    return response

#documentation
@app.route('/documentation')
def documentation():
    doclist=JsonFile.loadData('./static/webdocs/index.json')
    return render_template('docs.html',docs=doclist["topics"])



#API ENDPOINTS
#dummy users
@app.route('/users/<profileType>/<number>')
def getUsersProfiles(profileType='fullprofile',number=10):
    usersData={"name":"Test"}
    if(profileType=='fullprofile'):
        pass
    elif(profileType=='miniprofile'):
        pass
    else:
        pass
    return jsonify(usersData)

#dummy products
@app.route('/products/<scope>/<number>')
def getProducts(scope='full',number=10):
    productData={"name":"Test"}
    if(scope=='fullproduct'):
        pass
    else:
        pass
    return jsonify(productData)

if __name__=="__main__":
    app.run(debug=True)