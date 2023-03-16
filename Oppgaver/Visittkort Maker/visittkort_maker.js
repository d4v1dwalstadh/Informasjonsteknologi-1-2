let body = document.getElementsByTagName("body")[0]

//visittkort variabler
let visittkort = document.getElementById("visittkort");

//malene
let russekortMalImg = document.getElementById("russekortMal");
let visittkortMalImg = document.getElementById("visittkortMal");
let designEgenMalImg = document.getElementById("designEgenMal");

//design egen variabler
let designEgenInfo = document.getElementById("designEgenInfo");
let helRammeRadio = document.getElementById("helRammeRadio");
let stipletRammeRadio = document.getElementById("stipletRammeRadio");
let ingenRammeRadio = document.getElementById("ingenRammeRadio");
let designEgenKortet = document.getElementById("designEgenKortet");

let designEgenTittel = document.getElementById("designEgenTittel");
let designEgenAvsnitt = document.getElementById("designEgenAvsnitt");
let dinFarge = document.getElementById("dinFarge")

//russekort variabler
let altRussekort = document.getElementById("altRussekort");
let russekortet = document.querySelector("#russekortet");
let russekortInfo = document.getElementById("russekortInfo");
let rodRadio = document.getElementById("rodRadio");
let blaaRadio = document.getElementById("blaaRadio");
let velgBildeInp = document.getElementById("velgBildeInp");
let frmDinFil = document.getElementById("frmDinFil");
let russekortTittel = document.getElementById("russekortTittel");
let russekortBilde = document.getElementById("russekortBilde");
let bildeOpplastImg = document.getElementById("bildeOpplastImg");
let submitBildeInp = document.getElementById("submitBildeInp")

designEgenInfo.style.display = "none"
altRussekort.style.display = "none"
visittkort.style.display = "none"


//henter ut brukers fil som bilde til russekortet
function godtaFil(evt) {
  evt.preventDefault();
  filNavn = velgBildeInp.files[0].name
  russekortBilde.src = "./" + filNavn + ""
}
frmDinFil.addEventListener("submit", godtaFil) // funker ikke




function kjorRussekort() {
  visittkort.style.display = "none"
  designEgenInfo.style.display = "none"
  altRussekort.style.display = "block"
  rodRadio.checked = true
  russekortMalImg.style.border = "2px solid rgb(67, 214, 255)"
  visittkortMalImg.style.border = "2px solid #fff"
  designEgenMalImg.style.border = "2px solid #fff"

  blaaRadio.onclick = function () {
    russekortet.setAttribute("id", "russekortetBlaa")
    russekortTittel.src = "./blaaruss.tittel.png"
  }
  rodRadio.onclick = function () {
    russekortet.setAttribute("id", "russekortet")
    russekortTittel.src = "./rodruss.tittel.png"
  }
}
russekortMalImg.addEventListener("click", kjorRussekort);

function byttBakgrunnsbilde() {
  velgBildeInp.click()
  velgBildeInp.onchange = function () {
    submitBildeInp.click()
  }
}
bildeOpplastImg.addEventListener("click", byttBakgrunnsbilde);


function kjorVisittkort() {
  altRussekort.style.display = "none"
  designEgenInfo.style.display = "none"
  visittkort.style.display = "block"
  russekortMalImg.style.border = "2px solid #fff"
  visittkortMalImg.style.border = "2px solid rgb(67, 214, 255)"
  designEgenMalImg.style.border = "2px solid #fff"
} //onclickk i html


//design selv delen
function kjorDesignSelv() {
  altRussekort.style.display = "none"
  visittkort.style.display = "none"
  designEgenInfo.style.display = "block"
  helRammeRadio.checked = true
  russekortMalImg.style.border = "2px solid #fff"
  visittkortMalImg.style.border = "2px solid #fff"
  designEgenMalImg.style.border = "2px solid rgb(67, 214, 255)"
} //onclick i html

helRammeRadio.onclick = function () {
  designEgenKortet.style.border = "1px solid black"
}
stipletRammeRadio.onclick = function () {
  designEgenKortet.style.border = "2px dotted black"
}
ingenRammeRadio.onclick = function () {
  designEgenKortet.style.border = "1px solid white"
}



//gjør divEL mulig å dra rundt
dragElement(document.getElementById("mydiv"));
dragElement(document.getElementById("mydiv2"));

function dragElement(elmnt) {
  var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
  if (document.getElementById(elmnt.id + "header")) {
    /* if present, the header is where you move the DIV from:*/
    document.getElementById(elmnt.id + "header").onmousedown = dragMouseDown;
  } else {
    /* otherwise, move the DIV from anywhere inside the DIV:*/
    elmnt.onmousedown = dragMouseDown;
  }

  function dragMouseDown(e) {
    e = e || window.event;
    e.preventDefault();
    // get the mouse cursor position at startup:
    pos3 = e.clientX;
    pos4 = e.clientY;
    document.onmouseup = closeDragElement;
    // call a function whenever the cursor moves:
    document.onmousemove = elementDrag;
  }

  function elementDrag(e) {
    e = e || window.event;
    e.preventDefault();
    // calculate the new cursor position:
    pos1 = pos3 - e.clientX;
    pos2 = pos4 - e.clientY;
    pos3 = e.clientX;
    pos4 = e.clientY;
    // set the element's new position:
    elmnt.style.top = (elmnt.offsetTop - pos2) + "px";
    elmnt.style.left = (elmnt.offsetLeft - pos1) + "px";
  }

  function closeDragElement() {
    /* stop moving when mouse button is released:*/
    document.onmouseup = null;
    document.onmousemove = null;
  }
}

//gjør editingen til divEL live
function dinDragEl(elementId, inpId) {
  document.getElementById(elementId).innerHTML = inpId.value
  if (document.getElementById(elementId).innerHTML == "") {
    document.getElementById(elementId).innerHTML = "Dra og flytt"
  }

}

function byttBakgrunnsfarge() {
  designEgenKortet.style.backgroundColor = dinFarge.value
}










