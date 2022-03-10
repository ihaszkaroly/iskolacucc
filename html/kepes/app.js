var nagykep = document.getElementById("nagykep");
var kepazo = [
    "kep1",
    "kep2",
    "kep3",
    "kep4",
    "kep5"
];
var kepnevek = [
    "kep1.jpg",
    "kep2.jpg",
    "kep3.jpg",
    "kep4.jpg",
    "kep5.jpg",
];

var kepek = [];

for(let i=0; i<kepazo.length ; i++){
    kepek.push(document.getElementById(kepazo[i]));
}
for(let i=0; i < kepek.length; i++){
    kepek[i].style.backgroundImage = "url(kepek/"+kepnevek[i]+")";
     set_img_pos(kepek[i],i);
}
function set_img_pos(kepazo, i){
    if(i<3){
        kepazo.style.left = (i * 100) + "px";
        kepazo.style.top = 0;
    }
    else{
        kepazo.style.top = ((i-2) * 100) + "px";
    }      
}
function set_lar_im(kepazo){
    nagykep.style.backgroundImage = kepazo.style.backgroundImage
}

for(let i = 0 ; i <kepek.length; i++){
    kepek[i].addEventListener("click", (event)=>{
        set_lar_im(event,target)
    });  
}