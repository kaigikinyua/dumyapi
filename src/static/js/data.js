const debug=true
let baseUrl="https://localhost:5000"
if(debug==false){
    url="https://hostedurl"
}
function message({type="error",msg}){
    var notification=document.getElementById("notification")
    notification.innerHTML=msg
    notification.classList.add(type)
    setTimeout(()=>{
        var notification=document.getElementById("notification")
        notification.classList.remove("error")
        notification.classList.remove("success")
        notification.classList.remove("warning")
    },5000)
    console.error(msg)
}

function getRequest(url,callback){
    fetch(baseUrl+url)
    .then(data=>res.json())
    .then(data=>{
        callback(data)
    })
    .catch((e)=>{
        message({type:"error",msg:`Could not fetch data from ${url}`})
    })
}
function postRequest({url,data,callback}){
    if(notNull(url) && notNull(data)){
        fetch(baseUrl+url,{
         method:"POST",
         body:data,
        }).then(res=>res.json())
        .then(data=>{
            callback(data)
        })
        .catch(e=>{
            message({type:"error",msg:`Got the error ${e} while posting data ${data} to ${baseUrl+url}`})
        })
    }else{
        var error=notNull(url)?`Url not Supplied value is ${url}`:`Please fill in the form`;
        message({type:"error",msg:error})
    }
}
function notNull(value){
    if(value!=undefined && value!=null && value!=""){
        return true;
    }else{
        return false;
    }
}

export{getRequest,postRequest,message}