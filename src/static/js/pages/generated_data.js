const submitBtn=document.getElementById("submit")
const textarea=document.getElementById("query")

submitBtn.addEventListener('click',(e)=>{
    postQuery(data=>{
        renderResult(data)
    })
});
textarea.addEventListener('keyup',(e)=>{
    if(textarea.value.length>0){
        submitBtn.disabled=false
    }
    else{
        submitBtn.disabled=true
    }
})
function postQuery(callback){
    var value=document.getElementById("query").value
    if(value.length>0){
        var data={"query":value}
        fetch(
            "http://localhost:5000/ddl",
            {
                method:"POST",
                body:JSON.stringify(data),
                contentType:'application/json'
            }
        )
        .then(res=>res.json())
        .then(data=>{callback(data)})
        .catch(e=>{
            console.log(e)
        });
    }else{
        //raise warning to indicate that the textarea is empty
    }
}

function renderResult(data){
    console.log(data)
    if(data!=undefined && data!=null){
        var output=document.getElementById("output")
        output.innerHTML=data["result"]
    }
}