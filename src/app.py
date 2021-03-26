from flask import Flask,render_template,jsonify,request
from models import GenericData
from utils import JsonFile
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

#generic data endpoint
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



#documentation
@app.route('/documentation')
def documentation():
    doclist=JsonFile.loadData('./static/webdocs/index.json')
    return render_template('docs.html',docs=doclist["topics"])


if __name__=="__main__":
    app.run(debug=True)