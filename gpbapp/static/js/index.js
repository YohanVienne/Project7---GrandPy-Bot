var form = document.querySelector("form");
var map = document.querySelector("#map");
var result = document.getElementById("result");


// Google Map initialize
function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 10,
        center: { lat: 48.856614, lng: 2.3522219 }
    });

    document.getElementById('submit').addEventListener('click', function () {
        var userQuestion = document.getElementById('userQuestion').value;
        requestQuestionMap( map, userQuestion);
    });
}

// Request the user question to the server and show item
function requestQuestionMap(map, userQuestion) {
    var reqQuestion = new XMLHttpRequest();
    var encodeVar = encodeURIComponent(userQuestion);
    reqQuestion.open("GET", "http://localhost:5000/question/" + encodeVar);
    reqQuestion.onreadystatechange = function () {
        if (reqQuestion.readyState == 4 && (reqQuestion.status >= 200 || reqQuestion.status == 0)) {
            var readData = JSON.parse(reqQuestion.responseText);
            
            
            // Show the map
            var location = new google.maps.LatLng(readData.lat, readData.lng);
            map.setCenter(location);
            var marker = new google.maps.Marker({
            map: map,
            position: (location),
            });

            // Show the Wiki Media text
            document.querySelector(".text").innerHTML = readData.story;
            var link = document.querySelector(".linkWiki");
            link.setAttribute('href', 'https://fr.wikipedia.org/wiki/' + readData.title);
        } else {
            wrongQuestion = "Je n'ai pas compris votre question";
            document.querySelector(".text").innerHTML = wrongQuestion;

        }
        result.style.display = "inline";
    };
    reqQuestion.send(null);
}