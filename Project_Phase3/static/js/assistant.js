window.onload = function(){
    myAnimals();
    checkRequests();
    checkDonations();
}

function myAnimals() {
    const xhttp = new XMLHttpRequest();
    const method = "GET";
    const url = "http://127.0.0.1:5000/assistant/myanimals";
    const async = true;

    xhttp.open(method, url, async);
    xhttp.send();
    xhttp.onload = function(){
        const data = JSON.parse(this.responseText);
        output = `<table class="table table-striped table-bordered">
                    <thead>
                        <tr>
                            <th>Animal ID</th>
                            <th>Animal Species</th>
                            <th>Animal Breed</th>
                            <th>Date of Birth</th>
                            <th>Arrival Cause</th>
                            <th>Status</th>
                            <th>Date Enrolled</th>
                        </tr>
                    </thead>`
                        

        for(i in data){
            output +=
                "<tr><td>" +
                data[i]["animal_id"] + 
                "</td><td>" +
                data[i]["animal_type"] +
                "</td><td>" +
                data[i]["animal_breed"] +
                "</td><td>" +
                data[i]["animal_dob"] +
                "</td><td>" +
                data[i]["arrival_cause"] +
                "</td><td>" +
                data[i]["status_comment"] +
                "</td><td>" +
                data[i]["date_enrolled"] +
                "</td></tr>";
        }
        output += `</table>`
        document.getElementById("myAnimals").innerHTML = output;
    }
}

function addVisit() {
    let customerID = document.getElementById("customerID").value;
    let animalID = document.getElementById("animalID").value;
    let vComment = document.getElementById("vComment").value;

    let auxJson = {"customer": customerID,
                "animal": animalID,
                "comment": vComment};
    let json = JSON.stringify(auxJson);

    const xhttp = new XMLHttpRequest();
    const method = "POST";
    const url = "http://127.0.0.1:5000/assistant/addvisits";
    const async = true;

    xhttp.open(method, url, async);
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.send(json);
    window.alert("Visit has been added.");
}

function checkRequests(){
    const xhttp = new XMLHttpRequest();
    const method = "GET";
    const url = "http://127.0.0.1:5000/assistant/requests";
    const async = true;

    xhttp.open(method, url, async);
    xhttp.send();
    xhttp.onload = function(){
        const data = JSON.parse(this.responseText);
        output = `<table class="table table-striped table-bordered">
                    <thead>
                        <tr>
                            <th>Request ID</th>
                            <th>Customer</th>
                            <th>Animal ID</th>
                        </tr>
                    </thead>`
        
        for (i in data){
            output +=
                "<tr><td>" +
                data[i]["request_id"] + 
                "</td><td>" +
                data[i]["customer_name"] +
                "</td><td>" +
                data[i]["animal_id"] +
                "</td></tr>";
        }

        output += "</table>"
        document.getElementById("checkRequests").innerHTML = output;
    }
}

function checkDonations(){
    const xhttp = new XMLHttpRequest();
    const method = "GET";
    const url = "http://127.0.0.1:5000/assistant/donations";
    const async = true;

    xhttp.open(method, url, async);
    xhttp.send();
    xhttp.onload = function(){
        const data = JSON.parse(this.responseText);
        output = `<table class="table table-striped table-bordered">
                    <thead>
                        <tr>
                            <th></th>
                            <th>Customer</th>
                            <th>Donated Amount</th>
                        </tr>
                    </thead>`
        
        for (i in data){
            output +=
                "<tr><td>" +
                data[i]["count"] +
                "</td><td>" +
                data[i]["customer_name"] +
                "</td><td>" +
                data[i]["money"] +
                "</td></tr>";
        }

        output += "</table>"
        document.getElementById("checkDonations").innerHTML = output;
    }
}

function searchAnimal(){
    let animal_id = document.getElementById("animalPass").value
    let res = ''
    let link = "http://127.0.0.1:5000/assistant/search/"

    res = link.concat(animal_id)
    fetch(res, {
        method: "GET"
    })
    .then((res) => {
        return res.json();
    })
    .then(function(json){
        jsondata = json;
        const keys = Object.keys(jsondata);

        var table = document.getElementById("animalPass");
    
        var rowCount = document.getElementById('animalPass').rows.length;
    
        if(rowCount == 0){
        }
        else{
            var Table = document.getElementById("animalPass");
            Table.innerHTML = "";
        }
    
      });
}

// function dropDown() {
//     document.getElementById("dropdown").classList.toggle("show");
// }