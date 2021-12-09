function currDogs() {
  const xhttp = new XMLHttpRequest();
  const method = "GET";
  const url = "http://127.0.0.1:5000/customer/currDogs";
  const async = true;
  xhttp.open(method, url, async);
  xhttp.send();
  xhttp.onload = function () {
    const html = JSON.parse(this.responseText);
    let text =
      "<table><tr><th>Animal ID</th><th>Animal Breed</th><th>Animal DOB</th><th>Date Enrolled</th></tr>";
    for (key in html) {
      text +=
        "<tr><td>" +
        html[key]["animal_id"] +
        "</td><td>" +
        html[key]["animal_breed"] +
        "</td><td>" +
        html[key]["animal_dob"] +
        "</td><td>" +
        html[key]["date_enrolled"] +
        "</td></tr>";
    }
    text += "</table>";
    document.getElementById("currentClasses").innerHTML = text;
  };
}

function currCats() {
  const xhttp = new XMLHttpRequest();
  const method = "GET";
  const url = "http://127.0.0.1:5000/customer/currCats";
  const async = true;
  xhttp.open(method, url, async);
  xhttp.send();
  xhttp.onload = function () {
    const html = JSON.parse(this.responseText);
    let text =
      "<table><tr><th>Animal ID</th><th>Animal Breed</th><th>Animal DOB</th><th>Date Enrolled</th></tr>";
    for (key in html) {
      text +=
        "<tr><td>" +
        html[key]["animal_id"] +
        "</td><td>" +
        html[key]["animal_breed"] +
        "</td><td>" +
        html[key]["animal_dob"] +
        "</td><td>" +
        html[key]["date_enrolled"] +
        "</td></tr>";
    }
    text += "</table>";
    document.getElementById("currentClasses").innerHTML = text;
  };
}

function underFive() {
  const xhttp = new XMLHttpRequest();
  const method = "GET";
  const url = "http://127.0.0.1:5000/customer/underFive";
  const async = true;
  xhttp.open(method, url, async);
  xhttp.send();
  xhttp.onload = function () {
    const html = JSON.parse(this.responseText);
    let text =
      "<table><tr><th>Animal ID</th><th>Animal Type</th><th>Animal Breed</th><th>Animal DOB</th><th>Date Enrolled</th></tr>";
    for (key in html) {
      text +=
        "<tr><td>" +
        html[key]["animal_id"] +
        "</td><td>" +
        html[key]["animal_type"] +
        "</td><td>" +
        html[key]["animal_breed"] +
        "</td><td>" +
        html[key]["animal_dob"] +
        "</td><td>" +
        html[key]["date_enrolled"] +
        "</td></tr>";
    }
    text += "</table>";
    document.getElementById("currentClasses").innerHTML = text;
  };
}

function overFive() {
  const xhttp = new XMLHttpRequest();
  const method = "GET";
  const url = "http://127.0.0.1:5000/customer/overFive";
  const async = true;
  xhttp.open(method, url, async);
  xhttp.send();
  xhttp.onload = function () {
    const html = JSON.parse(this.responseText);
    let text =
      "<table><tr><th>Animal ID</th><th>Animal Type</th><th>Animal Breed</th><th>Animal DOB</th><th>Date Enrolled</th></tr>";
    for (key in html) {
      text +=
        "<tr><td>" +
        html[key]["animal_id"] +
        "</td><td>" +
        html[key]["animal_type"] +
        "</td><td>" +
        html[key]["animal_breed"] +
        "</td><td>" +
        html[key]["animal_dob"] +
        "</td><td>" +
        html[key]["date_enrolled"] +
        "</td></tr>";
    }
    text += "</table>";
    document.getElementById("currentClasses").innerHTML = text;
  };
}


function requestVisit()
{
  var animal_id = document.getElementById("Newname").value

  
  fetch("http://127.0.0.1:5000/student/requestVisit", {
    method: `POST`,
    body: JSON.stringify({animal_id:animal_id
    }),
    headers: {
        "Content-type": "application/json charset=UTF-8"
    }
})
.then(function (response) {
  if (response.status !== 200) {
    console.log(`Looks like there was a problem. Status code: ${response.status}`);
    var table = document.getElementById("Addedbody");
    var rowCount = document.getElementById("Addedbody").rows.length;
    if (rowCount == 0 ){}
    else{
      var Table = document.getElementById("Addedbody");
      Table.innerHTML = "";
      console.log('')
    }
    var row = `<tr>
                            <td>The animal you requested is currently not available for visits please check its current status for reasoning.</td>
                      </tr>`;
        table.innerHTML += row;
    return;
  }
  else
  {
    var table = document.getElementById("Addedbody");
    var rowCount = document.getElementById("Addedbody").rows.length;
    if (rowCount == 0 ){}
    else{
      var Table = document.getElementById("Addedbody");
      Table.innerHTML = "";
    }
    var row = `<tr>
                            <td>Successfully Requested.</td>
                      </tr>`;
        table.innerHTML += row;
  }
  response.json().then(function (data) {
    console.log(data);
  });
})
.catch(function (error) {
  console.log("Fetch error: " + error);
});
}


function makeDonation()
{
  var donation_amount = document.getElementById("Amount").value
  fetch("http://127.0.0.1:5000/customer/makeDonation", {
    method: `POST`,
    body: JSON.stringify({donation_amount:donation_amount
    }),
    headers: {
        "Content-type": "application/json charset=UTF-8"
    }
})
.then(function (response) {
  if (response.status !== 200) {
    console.log(`Looks like there was a problem. Status code: ${response.status}`);
    return;
  }
  response.json().then(function (data) {
    console.log(data);
  });
})
.catch(function (error) {
  console.log("Fetch error: " + error);
});

}


function getOutcome()
{
      var animal_id = document.getElementById("DisplayOutcome").value;
      let res = ''
      var link = "http://127.0.0.1:5000/customer/getOutcome/"
      res = link.concat(animal_id)
      console.log(res)
      fetch(res, {
        method: `GET`
    })
      .then((res) => {
        return res.json();
      })
      .then(function (json) {
        jsondata = json;
        console.log(jsondata)
        const keys = Object.keys(jsondata);
  
        var table = document.getElementById("Outcomebody");
    
        var rowCount = document.getElementById('Outcomebody').rows.length;
    
        if(rowCount == 0){
        }
        else{
            var Table = document.getElementById("Outcomebody");
            Table.innerHTML = "";
        }
    
        var row = `<tr>
                            <td>Current Status: ${jsondata[animal_id]}</td>
                      </tr>`;
        table.innerHTML += row;
      });

}
