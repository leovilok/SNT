
<script type="text/javascript">

const questions = {
    distance : {
        dist1 : 30000,
    },
    coordinates : {
        coordlat1 : 20,
        coordlat2 : "S",
        coordlon1 : 30,
        coordlon2 : "E",
    },
};

satellites = [
    {
        x: 300,
        y: 40,
        dst: 40,
        name: "A",
        color: "red",
    },
    {
        x: 220,
        y: 200,
        dst: 40,
        name: "B",
        color: "royalblue",
    },
    {
        x: 640,
        y: 180,
        dst: 40,
        name: "C",
        color: "lawngreen",
    },
];

answers = {};

API = window.API || window.parent.API;

window.onload = function() {
    if (API) {
        API.LMSInitialize("");

        suspend_data = API.LMSGetValue("cmi.suspend_data");

        if (suspend_data) {
            answers = JSON.parse(suspend_data);
        }

        for (id in answers) {
            document.getElementById(id).value = answers[id];
        }
    }

    canvasctx = document.getElementById('map').getContext('2d');

    sat_img = new Image();
    sat_img.src = "gps-sat.png";

    bg_img = new Image();
    bg_img.src = "equirect-map-bg.png";
    bg_img.onload = redraw_canvas;
}

function drawcircle(x,y,r,fill,stroke) {
    canvasctx.beginPath();
    canvasctx.arc(x, y, r, 0, 2 * Math.PI, false);

    if (fill) {
        canvasctx.fillStyle = fill;
        canvasctx.fill();
    }

    if (stroke) {
        canvasctx.lineWidth = 2;
        canvasctx.strokeStyle = stroke;
        canvasctx.stroke();
    }
}

function redraw_canvas() {
    canvasctx.drawImage(bg_img, 0, 0);
    for (i in satellites) {
        sat = satellites[i];
        drawcircle(sat.x, sat.y, sat.dst, false, sat.color);
        canvasctx.drawImage(sat_img, sat.x-32, sat.y-32);
        canvasctx.fillStyle = sat.color;
        canvasctx.textAlign = "center";
        canvasctx.textBaseline = "middle";
        canvasctx.font = "bold 20px Sans";
        canvasctx.fillText(sat.name, sat.x, sat.y);
    }
}

function score() {
    var count = 0;
    var correct = 0;
    for (qid in questions) {
        for (id in questions[qid]) {
            count++;
            if (questions[qid][id] == answers[id])
                correct++;
        }
    }

    return correct*100/count;
}

function satslide(num, val) {
    satellites[num].dst = val;
    document.getElementById("satdstlabel"+num).innerHTML = val;
    redraw_canvas();
}

function validate(questions) {
    for (id in questions) {
        var rep = document.getElementById(id);

        if (rep.value){
            answers[id] = rep.value.replace(',', '.').trim().toUpperCase();
            if (answers[id] == questions[id]) {
                rep.style.backgroundColor='green';
            } else {
                rep.style.backgroundColor='red';
            }
        }
    }

    if (API) {
        API.LMSSetValue("cmi.core.score.raw", score());
        API.LMSSetValue("cmi.suspend_data", JSON.stringify(answers));
        API.LMSSetValue("cmi.core.score.lesson_status", "completed");

        API.LMSCommit("");
    }
}

function nextSCO() {
    if (API) {
        API.LMSSetValue("nav.event","continue"); // Probably Moodle specific
        API.LMSFinish("");
    }
}

</script>

# Trilatération

La **trilatération** permet de déduire la position d'un point grâce à sa
distance avec 3 autres points dont on connaît déjà la position.
Dans le système GPS les satellites envoient régulièrement :

- leur coordonnées précises ;
- l'heure à laquelle ils envoient les données.

En recevant ces messages de 3 satellites ou plus, et en connaissant l'heure
précise de réception des messages, on peut retrouver notre position.

Voyons d'abord comment mesurer la distance qui nous sépare d'un satellite.

## Distance

Quand on reçoit un message d'un satellite on connaît :

- **l'heure précise d'envoi** du message, puisque le satellite la met dans le
  message et qu'il embarque une horloge atomique ;
- **l'heure précise d'arrivée** du message, à condition d'avoir une horloge
  bien à l'heure.

La différence entre ces 2 heures est le temps que le message à mis à parcourir
l'espace entre l'émétteur (le satellite) et le récepteur GPS.

Par exemple si un message est :

- envoyé à *19 heures 23 minutes 05 secondes et **230** millisecondes*
- reçu à *19 heures 23 minutes 05 secondes et **683** millisecondes*

Il aura mis 683 - 230 = 453 ms à arriver.

![](temps.png)

Comme le message est envoyé par onde radio, il se déplace à la vitesse de la
lumière, donc à peu près 300km/ms.

Dans notre exemple, on est donc à $453\times300=135900$ km du satellite.

### Question :

Si on reçoit le message d'un satellite :

- envoyé à *13 heures 37 minutes 42 secondes et **100** millisecondes*
- reçu à *13 heures 37 minutes 42 secondes et **200** millisecondes*

Donnez la **distance** (en km) qui nous sépare du satellite :

*(en considérant toujours que le message se déplace à 300km/ms)*

<input id="dist1" type="number" size="10" step="10" min="0" title="Distance en km">
</input>
km 
<button onclick="validate(questions.distance);">
Valider
</button>

## Trilatération

Si on connaît notre distance à **un seul** satellite, et les coordonnées de ce
satellite, on ne peut pas connaître notre position exacte, mais on sait qu'on
est sur le cercle qui a pour centre le satellite et pour rayon cette distance.

Par exemple ici on pourraît être n'importe où sur le cercle orange :

![](trilat-1.png)

Si on connait la position et la distance à **2** satellites, il ne reste que
2 possibilités : les 2 points où les cercles se croisent.

Exemple :

![](trilat-2.png)

Donc pour connaître notre position exacte on a besoin de **3 satellites**.
Les 3 cercles qui ont pour centre les satellites et pour rayon la distance
entre le satellite et le récepteur se croisent en un point aui est à la
position exacte du récepteur. Cette méthode s'appelle la **trilatération**.

Exemple :

![](trilat-3.png)

En réalité dans le système GPS il y a toujours au minimum 4 satellites dont on
reçoit les message à tout moment : ça permet d'être plus précis, notamment si
on n'est pas sûr que l'horloge d'un appareil est suffisement précise.

### Question :


On veut trouver notre position grâce au système GPS. On capte les messages des 3 satellites
A, B, et C.

En comparant l'heure d'arrivée et de départ des messages reçus on en déduit que :

- **A** est à 216 ms de nous,
- **B** est à 201 ms de nous,
- **C** est à 223 ms de nous.

Grâce aux coordonnées contenues dans les messages des satellites, on a pu les
replacer sur une carte :

<canvas id="map" width="720" height="360">
</canvas>

Vous pouvez régler l'affichage des distances des satellites grâce aux
glissières suivantes :

Distance au satellite **A** : 
<input type="range" min="0" max="360" defaultValue="40" oninput="satslide(0, this.value);">
</input>
[40]{#satdstlabel0} ms.

Distance au satellite **B** : 
<input type="range" min="0" max="360" defaultValue="40" oninput="satslide(1, this.value);">
</input>
[40]{#satdstlabel1} ms.

Distance au satellite **C** : 
<input type="range" min="0" max="360" defaultValue="40" oninput="satslide(2, this.value);">
</input>
[40]{#satdstlabel2} ms.

Trouvez la position de notre récepteur GPS par **trilatération**.

Déduisez-en les **coordonnées géographiques** de notre récepteur :

*(Rappel : les lignes horizontales et verticales sont placées tous les 10°)*

<input id="coordlat1" type="number" size="3" step="10" min="0" max="180" title="Latitude">
</input>
°
<input id="coordlat2" type="text" size="1" maxlength="1" pattern="[sSnNeEwWoO]" title="Latitude">
</input>
,
<input id="coordlon1" type="number" size="3" step="10" min="0" max="180" title="Longitude">
</input>
°
<input id="coordlon2" type="text" size="1" maxlength="1" pattern="[sSnNeEwWoO]" title="Longitude">
</input>

<button onclick="validate(questions.coordinates);">
Valider
</button>

