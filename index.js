import seallist from './seals.js';

let gridDiv = document.getElementById("grid");
let template = `
<div class="gridbox" id="!ID">
    <img class="sealimg" src="!PATH">
    !NAME
</div>
`;

let drawlist = Array.from(seallist);
let currentdrawn = drawlist;
drawArray(currentdrawn);


//Tags
let military = document.getElementById("militarybox");
let state = document.getElementById("statebox");
let federal = document.getElementById("federalbox");
let tribal = document.getElementById("tribalbox");
let historical = document.getElementById("historicalbox");
let searchbox = document.getElementById("searchbar");


military.addEventListener('change', drawSeals);
state.addEventListener('change', drawSeals);
federal.addEventListener('change', drawSeals);
tribal.addEventListener('change', drawSeals);
historical.addEventListener('change', drawSeals);
searchbox.addEventListener('input', drawSeals);

const checkboxes = document.querySelectorAll('input[type="checkbox"]');
checkboxes.forEach(checkbox => {
    checkbox.checked = true;
});



function filterSeals() {
        return seallist.filter((seal) => {
            let searchfilter

            if (searchbox.value == null) { searchfilter = "" }
            else searchfilter = searchbox.value.toLowerCase();

            return (seal.title.toLowerCase().includes(searchfilter) && (
                seal.tags.includes("Military") && military.checked ||
                seal.tags.includes("Federal") && federal.checked ||
                seal.tags.includes("State") && state.checked ||
                seal.tags.includes("Tribal") && tribal.checked ||
                seal.tags.includes("Historical") && historical.checked)
            )
        });
    }

function fadeSeal(id) {
        document.getElementById(id).classList.add('fade-out');
    }

function sealEqual(seal1, seal2) {
        return seal1.id == seal2.id;
    }


function drawSeals() {
        //seals that ought to be displayed
        let filteredseals = filterSeals();

        //fadeaway transition
        let subtractedSeals = currentdrawn.filter(seal1 => !filteredseals.some(seal2 => sealEqual(seal1, seal2)));


        console.log("Seals to remove", subtractedSeals);

        subtractedSeals.forEach(seal => {
            
            seal = document.getElementById(seal.id);
            seal.classList.add('hideme');

        });

        // Seals that need to be added to the display
        let drawSeals = filteredseals.filter(seal1 => !currentdrawn.some(seal2 => sealEqual(seal1, seal2)));
        //drawArray(drawSeals);

        drawSeals.forEach(seal => {
            document.getElementById(seal.id).classList.remove('hideme');
        })
        currentdrawn = filteredseals;

    }

function drawArray(sealArray) {
        sealArray.forEach(element => {
            let currentSealHTML = template.replace("!ID", element.id);
            currentSealHTML = currentSealHTML.replace("!PATH", element.path);
            currentSealHTML = currentSealHTML.replace("!NAME", element.title);
            gridDiv.innerHTML += currentSealHTML;
        });


    }

console.log("loading...");


drawSeals();
