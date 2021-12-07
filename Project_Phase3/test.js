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