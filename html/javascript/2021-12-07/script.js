const atmeroelem = document.querySelector("#atmero");
const szamitgomb = document.querySelector("#szamitgomb");
const eredmenyelem = document.querySelector("#eredmeny")

szamitgomb.addEventListener("click",event =>{
    let atmero = Number(atmeroelem.value);
    let sugar = atmero / 2;
    let terulet = Math.pow(sugar , 2) * Math.PI;
    let teruletfele = terulet / 2
    eredmenyelem.value = teruletfele + " m²"
})