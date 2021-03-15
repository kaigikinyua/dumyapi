var prevPageYOffset=0
var topnav=document.getElementById("topnav")
window.onscroll=()=>{
    if(prevPageYOffset-pageYOffset>0){
        //showtopnav
        setTimeout(showTopNav(),700)
    }else{
        //hidetopnav
        setTimeout(hideTopNav(),700)
    }
    prevPageYOffset=pageYOffset
}
function hideTopNav(){
    topnav.classList.remove("topnavshow")
    topnav.classList.add("topnavhide")
}
function showTopNav(){
    topnav.classList.remove("topnavhide")
    topnav.classList.add("topnavshow")
}