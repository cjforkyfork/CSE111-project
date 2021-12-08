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

function editAnimals() {
    let animal_id = document.getElementById("animalID").value
    

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

// function dropDown() {
//     document.getElementById("dropdown").classList.toggle("show");
// }