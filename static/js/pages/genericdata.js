var generic_data=new Vue({
    el:"#selected_data",
    delimiters:['[[',']]'],
    data:{
        title:"Users",
        endpoint:"https://localhost:5000/users",
        raw_data:[
            {"username": "Rosemary Einstein", "firstname": "Rosemary", "lastname": "Einstein", "email": "rosemaryeinstein@dev.org", "password": "abcdefghijklm12345678!@#$%", "phone": "+4340795988"},
            {"username": "Kimberly Tlkmuch", "firstname": "Kimberly", "lastname": "Tlkmuch", "email": "kimberlytlkmuch@example.com", "password": "abcdefghijklmnopqrst12345678!@#$", "phone": "+3628527252"}
        ]
    },
})
//update the generic data
function updateGenericData(){
    fetch_Data("http://localhost:5500/testdata.json",
    (state,data)=>{
        if(state==true){
            generic_data.title=data.title
            generic_data.endpoint=data.endpoint
            generic_data.raw_data=data.data
        }
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
