alert("Helló világ!");
console.log("ide is lehet");

const cim = document.getElementById('cim');
const valtGomb = document.getElementById("valtGomb");

valtGomb.addEventListener('click',function(){
    var szin = cim.style.color;
    if (szin != "white"){
        cim.style.backgroundColor = "red"
        cim.style.color = "white"
    }else{
        cim.style.backgroundColor = "white"
        cim.style.color = "black"
    }
})