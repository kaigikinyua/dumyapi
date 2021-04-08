const submitBtn=document.getElementById("submit")
submitBtn.addEventListener('click',(e)=>{
    postQuery()
})
function postQuery(){
    var data={"query":document.getElementById("query").value}
    fetch(
        "http://localhost:5000/generateddata",
        {
            method:"POST",
            body:JSON.stringify(data),
            contentType:'application/json'
        }
    )
    .then(res=>res.json())
    .then(data=>{console.log(data)})
    .catch(e=>{
        console.log(e)
    })
}