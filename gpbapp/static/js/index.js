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
        address = requestQuestion(document.getElementById('userQuestion').value);
        console.log(address);
        //geocodeAddress(geocoder, map, address);
    });
}

// Request the user question to the API
function requestQuestion(userQuestion) {
    var reqQuestion = new XMLHttpRequest();
    var encodeVar = encodeURIComponent(userQuestion);
    reqQuestion.open("POST", "http://localhost:5000/question");
    reqQuestion.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    reqQuestion.onreadystatechange = function () {
        if (reqQuestion.readyState == 4 && (reqQuestion.status >= 200 || reqQuestion.status == 0)) {
            return reqQuestion.responseText;
        }
    };
    reqQuestion.send('question=' + encodeVar);

}


function geocodeAddress(geocoder, resultsMap, address) {
    geocoder.geocode({'address' : address}, function(results, status) {
        if (status === 'OK') {
            resultsMap.setCenter(results[0].geometry.location);
            var marker = new google.maps.Marker({
            map: resultsMap,
            position: results[0].geometry.location
        });
        } else {
            alert('Geocode was not successful for the following reason: ' + status);
        }
    });
}