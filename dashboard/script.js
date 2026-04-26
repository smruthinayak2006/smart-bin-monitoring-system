function updateBars(){

let fills =
document.querySelectorAll(".fill");

fills.forEach(function(bar){

let value=
Math.floor(
60 + Math.random()*40
);

bar.style.width=
value+"%";

});

}

setInterval(
updateBars,
3000
);