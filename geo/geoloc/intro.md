<script type="text/javascript">
API = window.API || window.parent.API;

if (API) {
    API.LMSInitialize("");
}

function nextSCO() {
    if(API) {
        API.LMSSetValue("nav.event","continue"); // Probably Moodle specific
        API.LMSFinish("");
    }
}

</script>

# Géolocalisation par satellite

La géolocalisation permet de connaître sa **position** dans le monde et de la
replacer sur une carte numérique.

On cherche à retrouver nos **coordonnées géographiques** en se servant de la
position et la distance de plusieurs satellites.

Dans le système **GPS** par exemple, une trentaine de satellites orbitent
autour de la terre pour qu'il y ai toujours au moins 4 satellites dans le
dans le ciel au dessus de chaque point de la terre.

![Satellites visibles depuis un point (Image sous licence CC-BY-SA par Paulsava)](GPS24goldenSML-CCBYSA-Paulsava.gif)

Mais d'abord pour pouvoir placer un point sur une carte, on a besoin de ses
coordonnées gaographiques : 
<button onclick="nextSCO();">
Commencer l'activité : coordonnées
</button>

