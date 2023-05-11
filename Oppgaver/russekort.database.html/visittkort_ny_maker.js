

let body = document.getElementsByTagName("body")[0]

//russekort variabler
let altRussekort = document.getElementById("altRussekort");
let russekortet = document.querySelector("#russekortet");
let russekortInfo = document.getElementById("russekortInfo");
let rodRadio = document.getElementById("rodRadio");
let blaaRadio = document.getElementById("blaaRadio");
let velgBildeInp = document.getElementById("velgBildeInp");
let frmDinFil = document.getElementById("frmDinFil");
let russekortTopplinjen = document.getElementById("russekortTopplinjen");
let russekortTittel = document.getElementById("russekortTittel");
let russekortAdresse = document.getElementById("russekortAdresse");
let russekortTlf = document.getElementById("russekortTlf");
let russekortNavn = document.getElementById("russekortNavn");
let russekortQuote = document.getElementById("russekortQuote");
let russekortBilde = document.getElementById("russekortBilde");
let bildeOpplastImg = document.getElementById("bildeOpplastImg");
let submitBildeInp = document.getElementById("submitBildeInp")

let minListe = document.getElementById("minListe");

altRussekort.style.display = "block"
rodRadio.checked = true



for (let el in russekortOptions.personer) {
  minListe.innerHTML += "<option>" + russekortOptions.personer[el].navn + "</option>"
}


function fyllRussekortInfo(personNr) {
  russekortTopplinjen.innerHTML = russekortOptions.personer[personNr].skole
  russekortNavn.innerHTML = russekortOptions.personer[personNr].navn
  russekortAdresse.innerHTML = "adr: " + russekortOptions.personer[personNr].adresse
  russekortTlf.innerHTML = "tlf: " + russekortOptions.personer[personNr].tlf
  russekortQuote.innerHTML = russekortOptions.personer[personNr].quote
  russekortBilde.src = russekortOptions.personer[personNr].bilde
  if (russekortOptions.personer[personNr].farge == "rod") {
    russekortTittel.src = "./rodruss.tittel.png"
    rodRadio.click()
    rodRadio.checked = true
  }
  if (russekortOptions.personer[personNr].farge == "blaa") {
    russekortTittel.src = "./blaaruss.tittel.png"
    blaaRadio.click()
    blaaRadio.checked = true
  }
}
minListe.addEventListener("change", function () { fyllRussekortInfo(minListe.selectedIndex - 1) })


/*lar brukeren velge farge på russekortet ved hjelp av radioknapper
når knapp trykkes byttes classes på russekort-diven til en allerede 
laget klasse som egnes for gitte fargen*/
blaaRadio.onclick = function () {
  russekortet.setAttribute("id", "russekortetBlaa")
  russekortTittel.src = "./blaaruss.tittel.png"
}
rodRadio.onclick = function () {
  russekortet.setAttribute("id", "russekortet")
  russekortTittel.src = "./rodruss.tittel.png"
}

//henter ut brukers fil som bilde til russekortet
function godtaFil(evt) {
  evt.preventDefault();
  filNavn = velgBildeInp.files[0]
  russekortBilde.src = URL.createObjectURL(filNavn)
}
frmDinFil.addEventListener("submit", godtaFil) // funker ikke

/*lar bruker trykke på input[type=file] ved å trykke på et kameraikon først
funksjonen trykker også automatisk på submit knapp slik at etter bilde er valgt 
kommer det rett inn på kortet*/
function byttBakgrunnsbilde() {
  velgBildeInp.click()
  velgBildeInp.onchange = function () {
    submitBildeInp.click()
  }
}
bildeOpplastImg.addEventListener("click", byttBakgrunnsbilde);


















