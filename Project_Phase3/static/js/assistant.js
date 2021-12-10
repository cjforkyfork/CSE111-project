window.onload = function(){
    myAnimals();
    checkStatus();
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
        output = `<table class="table table-striped table-bordered" style="max-width: 85%; margin-left: auto; margin-right: auto;">
                    <thead>
                        <th class="table-header" colspan="100%">My Animal(s)</th>
                    </thead>
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
    let statusKey = document.getElementById("statusKey").value;

    let auxJson = {"customer": customerID,
                "animal": animalID,
                "comment": vComment,
                "status": statusKey};
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

function fill(){
    let animalID = document.getElementById("animalID_E").value;
    let res = ''
    let link = "http://127.0.0.1:5000/assistant/fill/"

    res = link.concat(animalID)
    fetch(res, {
        method: 'GET'
    })
    .then((res) => {
        return res.json();
      })
      .then(function (json) {
        let result = document.getElementById("filledResults");
    
        let rowCount = document.getElementById("filledResults").rows.length;
        // window.alert(rowCount);
    
        if(rowCount == 0){
            // proceed forward
        }
        else{
            // already has content, sets it back to row count = 0
            let auxResult = document.getElementById("filledResults");
            auxResult.innerHTML = "";
        }
    
        let output = `<tr>
                        <td style="padding-left: 3rem;">
                            <div class="row" style="padding: 1rem;">
                                <div class="col-6">
                                    <div class="row">
                                        <label class="labelinput">Arrival Cause: </label>
                                        <input class="input" type="text" id="arrivalCause_E" name="arrivalCause_E" value="${json['arrival_cause']}">
                                    </div>
                                </div>
                                <div class="col-6">
                                    <div class="row">
                                        <label class="labelinput" style="padding-right: 1.15rem;">Date of Birth:</label>
                                        <input class="input" type="text" id="dob_E" name="dob_E" value="${json['animal_dob']}">
                                    </div>
                                </div>
                            </div>
                            <div class="row" style="padding: 1rem;">
                                <div class="col-6">
                                    <div class="row">
                                        <label class="labelinput" style="padding-right: 2.4rem;">Status Key:</label>
                                        <input class="input" type="text" id="statusKey_E" name="statusKey_E" value="${json['status_key']}">
                                    </div>
                                </div>
                                <div class="col-6">
                                    <div class="row">
                                        <label class="labelinput">Date Enrolled: </label>
                                        <input class="input" type="text" id="dateEnrolled_E" name="dateEnrolled_E" value="${json['date_enrolled']}">
                                    </div>
                                </div>
                            </div>
                            <div class="row" style="padding: 1rem;">
                                <label class="labelinput">Animal Breed: </label>
                                <input class="input" type="text" id="animalBreed_E" name="animalBreed_E" value="${json['animal_breed']}"  style="min-width:45%">
                            </div>
                            <div class="row" style="padding: 1rem;">
                                <input type="submit" name="submit" value="Submit" onclick="editAnimal()">
                            </div>
                        </td>
                    </tr>`;
        result.innerHTML += output;
      });  
}

function editAnimal(){
    let animalID = document.getElementById("animalID_E").value;
    let animalBreed = document.getElementById("animalBreed_E").value;
    let dob = document.getElementById("dob_E").value;
    let arrivalCause = document.getElementById("arrivalCause_E").value;
    let status = document.getElementById("statusKey_E").value;
    let dateEnrolled = document.getElementById("dateEnrolled_E").value;

    let auxJson = {"animalID": animalID,
                    "animalBreed": animalBreed,
                    "dob": dob,
                    "arrivalCause": arrivalCause,
                    "status": status,
                    "dateEnrolled": dateEnrolled}
    let json = JSON.stringify(auxJson);

    const xhttp = new XMLHttpRequest();
    const method = "POST";
    const url = "http://127.0.0.1:5000/assistant/editanimal";
    const async = true;

    xhttp.open(method, url, async);
    xhttp.setRequestHeader("Content-Type", "application/json");
    // window.alert(json)
    xhttp.send(json);
    window.alert("Animal has been updated.");
}

function checkStatus(){
    const xhttp = new XMLHttpRequest();
    const method = "GET";
    const url = "http://127.0.0.1:5000/assistant/status";
    const async = true;

    xhttp.open(method, url, async);
    xhttp.send();
    xhttp.onload = function(){
        const data = JSON.parse(this.responseText);
        output = `<table class="table table-striped table-bordered" style="margin-left: auto; margin-right: auto;">
                    <thead>
                        <tr>
                            <th>Status Key</th>
                            <th>Status Meaning</th>
                        </tr>
                    </thead>`
        
        for (i in data){
            output +=
                "<tr><td>" +
                data[i]["status"] + 
                "</td><td>" +
                data[i]["comment"] + 
                "</td></tr>";
        }

        output += "</table>"
        document.getElementById("checkStatus").innerHTML = output;
    }
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
        output = `<table class="table table-striped table-bordered" style="max-width: 75%; margin-left: auto; margin-right: auto;">
                    <thead>
                        <tr>
                            <th colspan="100%" class="table-header">Requests</th>
                        </tr>
                    </thead>
                    <thead>
                        <tr>
                            <th>Request ID</th>
                            <th>Member ID</th>
                            <th>Member Name</th>
                            <th>Animal ID</th>
                        </tr>
                    </thead>`
        
        for (i in data){
            output +=
                "<tr><td>" +
                data[i]["request_id"] + 
                "</td><td>" +
                data[i]["customer_id"] + 
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
        output = `<table class="table table-striped table-bordered" style="max-width:80%; margin-left: auto; margin-right: auto;">
                    <thead>
                        <tr>
                            <th>Member Name</th>
                            <th>Donated Amount</th>
                        </tr>
                    </thead>`
        
        for (i in data){
            output +=
                "<tr><td>" +
                data[i]["customer_name"] +
                "</td><td>" +
                data[i]["money"] +
                "</td></tr>";
        }

        output += "</table>"
        document.getElementById("checkDonations").innerHTML = output;
    }
}

// function dropDown() {
//     document.getElementById("dropdown").classList.toggle("show");
// }