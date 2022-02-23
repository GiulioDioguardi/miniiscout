// This example requires the Geometry library. Include the libraries=geometry
// parameter when you first load the API. For example:
// <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=geometry">
var marker;

function initMap() {
  const map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: 51.50461728424621, lng: 5.371673673893977 },
    zoom: 2,
  });

  var polygon = initPolygon(map)

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

function checkPosition() {

}
