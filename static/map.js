function initialize() {

  var updateMap = function (map, center) {
    map.setCenter(center);
    var marker = new google.maps.Marker({'map': map, 'position': center});
  };

  var map = new google.maps.Map(document.getElementById('map-canvas'), {
    'zoom': 14, 'center': new google.maps.LatLng(25.03518, 121.54388)   // CLBC.
  });

  var address = document.getElementById('location-content').innerHTML;

  var geocoder = new google.maps.Geocoder();
  geocoder.geocode({'address': address}, function(results, status) {
    if (status == google.maps.GeocoderStatus.OK && results.length) {
      updateMap(map, results[0].geometry.location);
    } else if (google.maps.places) {
      var service = new google.maps.places.PlacesService(map);
      var request = {'location': map.getCenter(), 'radius': 50000, 'query': address};
      service.textSearch(request, function (results, status) {
        if (status == google.maps.GeocoderStatus.OK && results.length)
          updateMap(map, results[0].geometry.location);
      });
    }
  });
}

google.maps.event.addDomListener(window, 'load', initialize);