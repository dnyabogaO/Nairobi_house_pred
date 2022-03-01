function getBedValue() {
    var uiBedrooms = document.getElementByName("uiBedrooms");
    for(var i in uiBedrooms) {
        if(uiBedrooms[i].checked) {
            return parseInt(i)+1;
        }
    }
    return -1; //invalid value
}

function getBathValue() {
    var uiBathrooms = document.getElementByName("uiBathrooms");
    for(var i in uiBathrooms) {
        if(uiBathrooms[i].checked) {
            return parseInt(i)+1;
        }
    }
    return -1; //invalid value
}

function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var Bedrooms = getBedValue();
    var Bathrooms = getBathValue();
    var sqft = document.getElementById("uiSqft");
    var location = document.getElementById("uiLocations");
    var estPrice = document.getElementById("uiEstimatedPrice");

    var url = "http://127.0.0.1:5000/predict_house_price";

    $.post(url, {
        Bedrooms: Bedrooms,
        bath: Bathrooms,
        total_sqft: parseFloat(sqft.value),
        location: locations.value

    },function(data,status) {
        console.log(data.estimated_price);
        estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + "Lakh</h2>";
        console.log(status);
    });

}

function onPageLoad() {
    console.log("document loaded");
    var url = "http://127.0.0.1:5000/get_location_names";
    $.get(url,function(data,status) {
        console.log("got response for get_location_names request");
        if(data) {
            var locations = data.locations;
            var uiLocations = document.getElementById("uiLocations");
            $('#uiLocations').empty();
            for(var i in locations) {
                var opt = new Option(locations[i]);
                $('#uiLocations').append(opt);
            }
        }
    });
}

window.onload = onPageLoad;