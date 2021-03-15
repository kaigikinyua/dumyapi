var genDataContainer=document.getElementById("generic_data_container")
var incrementing=false
window.onscroll=async()=>{
    incrementing_figures()
}
/*window.onload=async ()=>{
}*/
async function incrementing_figures(){
    if(window.pageYOffset+window.innerHeight>genDataContainer.offsetTop){
        if(incrementing==false){
            incrementing=true
            for (let i=0;i<100;i++){
                console.log("for loop")
                increment()
                await sleep(100)
            }
        }
    }else{
      //  console.log("condition not reached")
    }
}


async function increment(){
    var big_numbers=document.querySelectorAll("p.big_number")
    big_numbers.forEach(e=>{
        e.innerHTML=parseInt(e.innerHTML)+Math.floor(Math.random()*100)
})
}
function sleep(time){
    return new Promise(resolve=>setTimeout(resolve,time));
}