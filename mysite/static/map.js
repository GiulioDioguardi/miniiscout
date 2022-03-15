// This example requires the Geometry library. Include the libraries=geometry
// parameter when you first load the API. For example:
// <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=geometry">
var marker;
var polygon;

function setCookie(cname, cvalue, exdays) {
  const d = new Date();
  d.setTime(d.getTime() + (exdays*24*60*60*1000));
  let expires = "expires="+ d.toUTCString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function initMap() {
  const map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: 51.50461728424621, lng: 5.371673673893977 },
    zoom: 2,
    gestureHandling: 'greedy',
    streetViewControl: false,
    styles: [
      {
        featureType: "poi",
        stylers: [{ visibility: "off" }],
      },
      {
        featureType: "transit",
        elementType: "labels.icon",
        stylers: [{ visibility: "off" }],
      },
    ]
  });

  polygon = initPolygon(map)

  google.maps.event.addListener(map, "click", (e) => {
    if (marker && marker.setMap) {
      marker.setMap(null);
    }
    marker = new google.maps.Marker({
      position: e.latLng,
      map
    });
  });
}

function checkPosition(qTitleHash) {
    if (google.maps.geometry.poly.containsLocation(marker.position, polygon)) {
        alert("Goed gedaan! Dit is het juiste antwoord.\nJe vraag wordt als goed gemarkeerd en je keert terug naar de vragenlijst");
        //Write the hash of the title as a key for the cookie
        setCookie(qTitleHash, "FQzEhblF99", 2000)
        window.location.replace("/list");
      }
      else
      {
        alert("Dit is niet het juiste antwoord. Zet je pin op een andere plek en probeer het nog eens");
      }
}
