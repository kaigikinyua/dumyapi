var mainUrl="http://localhost:5000"
var generic_data=new Vue({
    el:"#selected_data",
    delimiters:['[[',']]'],
    data:{
        title:"Users",
        endpoint:"https://localhost:5000/users",
        structure:{},
        datastring:"",
        raw_data:[
            {"username": "Rosemary Einstein", "firstname": "Rosemary", "lastname": "Einstein", "email": "rosemaryeinstein@dev.org", "password": "abcdefghijklm12345678!@#$%", "phone": "+4340795988"},
            {"username": "Kimberly Tlkmuch", "firstname": "Kimberly", "lastname": "Tlkmuch", "email": "kimberlytlkmuch@example.com", "password": "abcdefghijklmnopqrst12345678!@#$", "phone": "+3628527252"}
        ],
    },
})
//update the generic data
function updateGenericData(title,subURL){
    var endp=`${mainUrl}${subURL}`
    fetch_Data(endp,
    (state,data)=>{
        generic_data.title=title
        generic_data.raw_data=data
        generic_data.endpoint=endp
        generic_data.structure=data[Object.keys(data)][0]
        //generic_data.datastring=jsonLinter(JSON.stringify(data))
        var d=document.getElementById('data')
        d.innerHTML=jsonLinter(JSON.stringify(data))
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

function jsonLinter(dataString){
    var square_stack=[];curly_stack=[];
    var lintedString='';
    for(var i=0;i<dataString.length;i++){
        var char=dataString[i]
        if(char=='['){
            //:[ | [
            lintedString+=`${tabs(square_stack.length)}<i class="square">${char}</i>\n${tabs(square_stack.length+1)}`
            square_stack.push(char)
        }else if(char=='{'){
            //:{} | {
            lintedString+=`<i class="curly">${char}</i>\n${tabs(square_stack.length+1)}`
            curly_stack.push(char)
        }else if(char=='}'){
            // }, | }
            lintedString+=`\n${tabs(square_stack.length+1)}<i class="curly">${char}</i>`

        }else if(char==']'){
            // ], | ]
            lintedString+=`\n${tabs(square_stack.length)}<i class='square'>${char}</i>\n`
            square_stack.pop()
        }else if(char==','){
            lintedString+=`${char}\n${tabs(square_stack.length+1)}`
        }else if(char==':'){
            lintedString+=` ${char} `
        }
        //add linting for 'key': | "key":
        else{
            lintedString+=char
        }
    }
    return lintedString
}
function tabs(number){
    var tabsString=''
    while(number>0){
        tabsString+="\t"
        number-=1
    }
    return tabsString
}
