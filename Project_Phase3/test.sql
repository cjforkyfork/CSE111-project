SELECT assistant_id, assistant_name
FROM shelter_assistant 
WHERE customer_id = 1
AND customer_name = 'Gerardino Cayetano Gonzalez'


SELECT animal_id,animal_type,animal_breed,animal_dob,animal.shelter_key,arrival_cause,status_key,date_enrolled
FROM animal
ORDER BY date_enrolled ASC

SELECT shelter_key
FROM shelter,customer
WHERE customer.customer_id = ?
AND customer.city_key = shelter.city_key

SELECT status_comment
FROM status, animal
WHERE animal.status_key = status.status_key
AND animal.animal_id = 1


SELECT animal_id,animal_type,animal_breed,animal_dob,animal.shelter_key,arrival_cause,status_key,date_enrolled
FROM animal
WHERE strftime('%Y-%m',animal_dob) = '2015-04'



select assistant_id,animal_id
from animals_assistant
where assistant_id = '?'

SELECT customer_name,SUM(money)
FROM customer,donations,shelter_assistant
WHERE customer.customer_id = donations.customer_id
AND shelter_assistant.assistant_id = '?'
AND shelter_assistant.shelter_key = donations.shelter_key
GROUP BY customer_name

SELECT request_id,customer_name,animal_id
FROM requests_visits,customer,shelter_assistant
WHERE requests_visits.customer_id = customer.customer_id
AND shelter_assistant.assistant_id = '?'
AND animal_id IN
(SELECT animal_id
FROM animals_assistant
WHERE assistant_id = '?')

UPDATE donations
SET shelter_key = '1'
WHERE customer_id = 'E'

DELETE FROM requests_visits
WHERE animal_id = 4

SELECT animal_id,animal_type,animal_breed,animal_dob,animal.shelter_key,arrival_cause,status_key,date_enrolled
FROM animal,customer,shelter
WHERE customer_id = 'A'
AND customer.city_key = shelter.city_key
AND animal.shelter_key = shelter.shelter_key
AND animal_type = 'Dog';

SELECT animal_id,animal_type,animal_breed,animal_dob,animal.shelter_key,arrival_cause,status_key,date_enrolled
FROM animal,customer,shelter
WHERE customer_id = 'B'
AND customer.city_key = shelter.city_key
AND animal.shelter_key = shelter.shelter_key
AND animal_type = 'Dog';

SELECT animal_id,animal_type,animal_breed,animal_dob,animal.shelter_key,arrival_cause,status_key,date_enrolled
FROM animal,customer,shelter
WHERE customer_id = 'C'
AND customer.city_key = shelter.city_key
AND animal.shelter_key = shelter.shelter_key
AND animal_type = 'Dog';

SELECT animal_id,animal_type,animal_breed,animal_dob,animal.shelter_key,arrival_cause,status_key,date_enrolled
FROM animal,customer,shelter
WHERE customer_id = 'D'
AND customer.city_key = shelter.city_key
AND animal.shelter_key = shelter.shelter_key
AND animal_type = 'Dog';

SELECT animal_id,animal_type,animal_breed,animal_dob,animal.shelter_key,arrival_cause,status_key,date_enrolled
FROM animal,customer,shelter
WHERE customer_id = 'E'
AND customer.city_key = shelter.city_key
AND animal.shelter_key = shelter.shelter_key
AND animal_type = 'Dog';

SELECT animal_id,animal_type,animal_breed,animal_dob,animal.shelter_key,arrival_cause,status_key,date_enrolled
FROM animal,customer,shelter
WHERE customer_id = 'Y'
AND customer.city_key = shelter.city_key
AND animal.shelter_key = shelter.shelter_key
AND animal_type = 'Dog';