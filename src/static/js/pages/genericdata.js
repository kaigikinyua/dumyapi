var mainUrl="http://localhost:5000"
//ui logic
function currentSelected(datasetIdentifier){
    var liTags=document.querySelectorAll('li.genericDataButton')
    liTags.forEach(t=>{
        if(t.dataset["litag"]==datasetIdentifier){
            t.classList.add('active')
        }else{
            t.classList.remove('active')
        }
    });
}

var generic_data=new Vue({
    el:"#selected_data",
    delimiters:['[[',']]'],
    data:{
        title:"",
        endpoint:"",
        structure:{},
        datastring:"",
        raw_data:[],
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
        currentSelected(title)
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
    var square_stack=[];curly_open=[],curly_close=[];
    var lintedString='';
    for(var i=0;i<dataString.length;i++){
        var char=dataString[i]
        if(char=='['){
            //:[ | [
            lintedString+=`${tabs(square_stack.length)}<i class="square">${char}</i>\n${tabs(square_stack.length+1)}`
            square_stack.push(char)
        }else if(char==']'){
            // ], | ]
            lintedString+=`\n${tabs(square_stack.length)}<i class='square'>${char}</i>\n`
            square_stack.pop()
        }else if(char=='{'){
            //:{} | {
            curly_open.push(char)
            var diff=curly_close.length-curly_open.length
            lintedString+=`${tabs(diff)}<i class="curly">${char}</i>\n${tabs(square_stack.length+1)}`
        }else if(char=='}'){
            // }, | }
            curly_close.push(char)
            var diff=curly_open.length-curly_close.length
            lintedString+=`\n${tabs(square_stack.length+diff-1)}<i class="curly">${char}</i>`
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
