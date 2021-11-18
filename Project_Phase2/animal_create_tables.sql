CREATE TABLE city(
city_key INT PRIMARY KEY NOT NULL,
city_name char(25) not null
);

CREATE TABLE shelter (
    shelter_key  INT PRIMARY KEY NOT NULL,
    shelter_name varchar(55) NOT NULL,
    city_key INT NOT NULL,
    FOREIGN KEY(city_key) REFERENCES city(city_key)
);
CREATE TABLE animal (
    animal_id  INT PRIMARY KEY NOT NULL,
    animal_type char(25) NOT NULL,
    animal_breed char(25) NOT NULL,
    animal_dob    date NOT NULL,
    shelter_key  INT NOT NULL,
    arrival_cause  varchar(55) NOT NULL,
    status_key   INT NOT NULL,
    date_enrolled date NOT NULL,
    FOREIGN KEY(status_key) REFERENCES status(status_key),
    FOREIGN KEY(shelter_key) REFERENCES shelter(shelter_key)
);
CREATE TABLE status (
    status_key INT PRIMARY KEY NOT NULL,
    status_comment char(25) NOT NULL
);
CREATE TABLE animals_assistant (
    assistant_id  INT NOT NULL,
    animal_id  INT NOT NULL,
    FOREIGN KEY(assistant_id) REFERENCES shelter_assistant(assistant_id),
    FOREIGN KEY(animal_id) REFERENCES animal(animal_id)
);
CREATE TABLE visits (
    visit_key   INT PRIMARY KEY NOT NULL,
    animal_id  INT  NOT NULL,
    status_key INT  NOT NULL,
    assistant_id INT  NOT NULL,
    visit_comment char(100)  NOT NULL,
    FOREIGN KEY(animal_id) REFERENCES animal(animal_id),
    FOREIGN KEY(status_key) REFERENCES status(status_key),
    FOREIGN KEY(assistant_id) REFERENCES shelter_assistant(assistant_id)
);
CREATE TABLE donations (
    donation_key INT PRIMARY KEY NOT NULL,
    customer_id  INT  NOT NULL,
    shelter_key  INT NOT NULL,
    money     decimal(9,2) NOT NULL,
    FOREIGN KEY(shelter_key) REFERENCES shelter(shelter_key)
);
CREATE TABLE shelter_assistant (
    assistant_id     INT PRIMARY KEY NOT NULL,
    assistant_name   varchar(55) NOT NULL,
    shelter_key     INT NOT NULL,
    FOREIGN KEY(shelter_key) REFERENCES shelter(shelter_key)
);

CREATE TABLE customer_community (
    customer_id    INT NOT NULL,
    shelter_key    INT NOT NULL,
    FOREIGN KEY(shelter_key) REFERENCES shelter(shelter_key)
    FOREIGN KEY(customer_id) REFERENCES customer(customer_id)
);

CREATE TABLE customer (
    customer_id  INT PRIMARY KEY NOT NULL,
    customer_name char(25) NOT NULL,
    city_key INT NOT NULL,
    FOREIGN KEY(city_key) REFERENCES city(city_key)
);

CREATE TABLE requests_visits (
    request_id INT NOT NULL,
    customer_id    INT NOT NULL,
    animal_id    INT NOT NULL,
    FOREIGN KEY(animal_id) REFERENCES shelter(animal_id)
    FOREIGN KEY(customer_id) REFERENCES customer(customer_id)
);