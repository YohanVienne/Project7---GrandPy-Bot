var form = document.querySelector("form");
var map = document.querySelector("#map");

////////////////////////////
// Google Map API function//
////////////////////////////

// Map Initialize
function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 10,
        center: { lat: 34.2331373, lng: -102.4107493}
    });
    var geocoder = new google.maps.Geocoder();

    document.getElementById('submit').addEventListener('click', function() {
        var userQuestion = document.getElementById('userQuestion').value;
        requestQuestionMap(geocoder, map, userQuestion);
    });
}

// Request the user question to the API
function requestQuestionMap(geocoder, map, userQuestion) {
    var reqQuestion = new XMLHttpRequest();
    var encodeVar = encodeURIComponent(userQuestion);
    reqQuestion.open("GET", "http://localhost:5000/question/" + encodeVar);
    reqQuestion.onreadystatechange = function () {
        if (reqQuestion.readyState == 4 && (reqQuestion.status >= 200 || reqQuestion.status == 0)) {
            var readData = reqQuestion.responseText;
            console.log("readDataMap: " + readData);
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
            position: results[0].geometry.location,
            });
        } else {
            alert("Je n'ai pas compris ta question ");
        }
    });
}

/////////////////////////
// Wiki Media function //
/////////////////////////

document.getElementById('submit').addEventListener('click', function () {
    var userQuestion = document.getElementById('userQuestion').value;
    requestQuestionWiki(userQuestion);
});

//Request the user_question to API
function requestQuestionWiki(userQuestion) {
    var reqQuestion = new XMLHttpRequest();
    var encodeVar = encodeURIComponent(userQuestion);
    reqQuestion.open("GET", "http://localhost:5000/wiki/" + encodeVar, true);
    reqQuestion.onreadystatechange = function () {
        if (reqQuestion.readyState == 4 && (reqQuestion.status >= 200 || reqQuestion.status == 0)) {
            var readData = JSON.parse(reqQuestion.responseText);
            dataOutput = readData.lat + "|" + readData.lng;
            console.log("readDataWiki: " + dataOutput);
            requestWiki(dataOutput);     
        }
    };
    reqQuestion.send(null);
}

//get the coordinate and search in Wiki Media geosearch function
function requestWiki(geo) {
    var reqWiki = new XMLHttpRequest();
    var url = "https://fr.wikipedia.org/w/api.php?action=query&format=json&uselang=fr&list=geosearch&gscoord=" + geo;
    reqWiki.open("GET", url, true);
    reqWiki.onreadystatechange = function () {
        if (reqWiki.readyState == 4 && (reqWiki.status >= 200 || reqWiki.status == 0)) {
            var readData = JSON.parse(reqWiki.responseText);
            var readDataCount = Object.keys(readData.query.geosearch).length;
            console.log("readDataCount: " + readDataCount);
            story(readDataCount, readData);
        }
    };    
    reqWiki.send(null);
}

// Get a random story about the geosearch
function story(readDataCount, readData) {
    var randomNumber = Math.floor(Math.random() * readDataCount);
    var pageid = readData.query.geosearch[randomNumber].pageid;
    console.log("random: " + randomNumber);
    var reqStory = new XMLHttpRequest();
    var url = "https://fr.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&utf8=1&formatversion=latest&exsentences=3&explaintext=1&exsectionformat=wiki&pageids=" + pageid;
    reqStory.open("GET", url, true);
    reqStory.onreadystatechange = function () {
        if (reqStory.readyState == 4 && (reqStory.status >= 200 || reqStory.status == 0)) {
            var result = JSON.parse(reqStory.responseText);
            console.log(result.query.pages[0].extract);
            var extractStory = result.query.pages[0].extract;
            var title = result.query.pages[0].title;
            writeStory(extractStory, title);
        }
    };
    reqStory.send(null);
}

//Write a random story on HTML page
function writeStory(extractStory, title) {
    document.querySelector(".text").innerHTML = extractStory;
    var link = document.querySelector(".linkWiki");
    link.setAttribute('href', 'https://fr.wikipedia.org/wiki/' + title);
    
}