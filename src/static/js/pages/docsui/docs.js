//setup doc view using vue
    //components -> appbar
    //page -> paragraph & titles

const baseURL="http://localhost:5000"

let contentvue=new Vue({
    el:'#docsview',
    delimiters:['[[',']]'],
    data(){
        return {
            title:'Test Title',
            content:[]
        }
    }
})

function renderDoc(doclink){
    fetchDocs(doclink,(data)=>{
        if(data.title && data.items){
            contentvue.title=data.title
            contentvue.content=data.items
        }
    })
}
function fetchDocs(url,callback){
    fetch(`${baseURL}${url}`)
    .then(res=>res.json())
    .then(data=>{callback(data)})
}


//search functionality
const searchInput=document.getElementById("search")
searchInput.addEventListener('keydown',(e)=>{
    var input=searchInput.value
    var tiles=document.querySelectorAll('div.tile')
    tiles.forEach(t=>{
        if(t.children[0].innerHTML.indexOf(input)==-1){
            t.style.display="none"
        }else{
            t.style.display="block"
        }
    })
})