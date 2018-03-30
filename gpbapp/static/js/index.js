var form = document.querySelector("form");
var map = document.querySelector("#map");

// Map Initialize
function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 10,
        center: {lat: -34.397, lng: 150.644}
    });
    var geocoder = new google.maps.Geocoder();

    document.getElementById('submit').addEventListener('click', function() {
        var userQuestion = document.getElementById('userQuestion').value;
        requestQuestion(geocoder, map, userQuestion);
    });
}

// Request the user question to the API
function requestQuestion(geocoder, map, userQuestion) {
    var reqQuestion = new XMLHttpRequest();
    var encodeVar = encodeURIComponent(userQuestion);
    reqQuestion.open("GET", "http://localhost:5000/question/" + encodeVar);
    reqQuestion.onreadystatechange = function () {
        if (reqQuestion.readyState == 4 && (reqQuestion.status >= 200 || reqQuestion.status == 0)) {
            var readData = reqQuestion.responseText;
            console.log("readData: " + readData);
            geocodeAddress(geocoder, map, readData);
        }
    };
    reqQuestion.send(null);
}

// Mark the position on map
function geocodeAddress(geocoder, resultsMap, address) {
    geocoder.geocode({'address' : address}, function(results, status) {
        if (status === 'OK') {
            resultsMap.setCenter(results[0].geometry.location);
            var marker = new google.maps.Marker({
            map: resultsMap,
            position: results[0].geometry.location
        });
        } else {
            alert("Je n'ai pas compris ta question ");
        }
    });
}