function myAnimals(){
    const xhttp = new XMLHttpRequest();
    const method = "GET";
    const url = "http://127.0.0.1:5000/assistant/myanimals";
    const async = true;

    xhttp.open(method, url, async);
    xhttp.send();
    xhttp.onload = function(){
        const data = JSON.parse(this.responseText);
        output = ""

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
        document.getElementById("myAnimals").innerHTML = output;
    }
}