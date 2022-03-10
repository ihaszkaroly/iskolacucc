const alapElem = document.querySelector("#alap");
const magassagElem  = document.querySelector("#magassag");
const teruletElem = document.querySelector("#terulet")
const gomb = document.querySelector("#szamit")

gomb.addEventListener("click",Event=>{
    let alap = Number(alapElem.value);
    let magassag = Number(magassagElem.value);
    let terulet = (alap*magassag)/2;
    teruletElem.value = terulet;

    alapElem.value = "";
    magassagElem.value = "";
})