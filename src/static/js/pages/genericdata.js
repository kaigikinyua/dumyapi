var mainUrl="http://localhost:5000"
var generic_data=new Vue({
    el:"#selected_data",
    delimiters:['[[',']]'],
    data:{
        title:"Users",
        endpoint:"https://localhost:5000/users",
        structure:{},
        raw_data:[
            {"username": "Rosemary Einstein", "firstname": "Rosemary", "lastname": "Einstein", "email": "rosemaryeinstein@dev.org", "password": "abcdefghijklm12345678!@#$%", "phone": "+4340795988"},
            {"username": "Kimberly Tlkmuch", "firstname": "Kimberly", "lastname": "Tlkmuch", "email": "kimberlytlkmuch@example.com", "password": "abcdefghijklmnopqrst12345678!@#$", "phone": "+3628527252"}
        ]
    },
})
//update the generic data
function updateGenericData(subURL){
    var endp=`${mainUrl}${subURL}`
    fetch_Data(endp,
    (state,data)=>{
        generic_data.raw_data=data
        generic_data.endpoint=endp
        generic_data.structure=data[Object.keys(data)][0]
    })
}

function fetch_Data(url,callback){
    fetch(url)
    .then(res=>res.json())
    .then(data=>{
        console.log(data)
        callback(true,data)
    })
    .catch(e=>{
        console.log(e)
        //show error notification
    })
}

function objectArray(object){
    if(Array.isArray(object)){
        var elementKeys=[]
        elementKeys=Object.keys(object[0])
        elementKeys.forEach((elem)=>{
            if(objectArray(object[0][elem]!=false)){elem=`${elem}:[]`}
        })
    }else{
        return false;
    }
}

function filterString(string){
    
}
