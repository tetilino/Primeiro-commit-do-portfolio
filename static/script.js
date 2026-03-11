document.addEventListener("DOMContentLoaded", function(){

const toggle = document.getElementById("toggle-theme")

if(toggle){

toggle.addEventListener("click", function(){

document.body.classList.toggle("light-mode")

if(document.body.classList.contains("light-mode")){
localStorage.setItem("theme","light")
toggle.innerHTML="☀"
}else{
localStorage.setItem("theme","dark")
toggle.innerHTML="🌙"
}

})

}

const theme = localStorage.getItem("theme")

if(theme === "light"){
document.body.classList.add("light-mode")
toggle.innerHTML="☀"
}

})

window.addEventListener("load", function () {
    const loader = document.getElementById("loader");
    if (loader) {
        loader.style.display = "none";
    }
});