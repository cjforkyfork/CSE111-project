-- Query all animals
SELECT animal_id, animal_type, animal_breed, animal_dob, arrival_cause, status_comment, date_enrolled
FROM animal
    INNER JOIN status ON status.status_key = animal.status_key

-- Query all animals specific to an assistant
SELECT animal.animal_id, animal_type, animal_breed, animal_dob, arrival_cause, status_comment, date_enrolled
FROM animal
    INNER JOIN status ON status.status_key = animal.status_key
    INNER JOIN animals_assistant ON animals_assistant.animal_id = animal.animal_id
    INNER JOIN shelter_assistant ON shelter_assistant.assistant_id = animals_assistant.assistant_id
WHERE shelter_assistant.assistant_name = 'Tim Elliot'

-- Query requests specific to the animals assigned
SELECT request_id, customer_name, animal_id
FROM requests_visits
    INNER JOIN customer ON customer.customer_id = requests_visits.customer_id,
    shelter_assistant
WHERE shelter_assistant.assistant_id = 'A' AND
    animal_id IN
            (SELECT animal_id
            FROM animals_assistant
            WHERE assistant_id = 'A')

-- Check donations to a specific shelter
SELECT DISTINCT customer_name, SUM(money), donations.shelter_key, COUNT(1)
FROM donations
    INNER JOIN customer ON customer.customer_id = donations.customer_id
    INNER JOIN shelter_assistant ON shelter_assistant.shelter_key = donations.shelter_key
WHERE assistant_id = 'A'
-- GROUP BY donations.customer_id

-- Retrieving animal
SELECT *
FROM animal
WHERE animal_id = 2

-- Inserting a new visit
INSERT INTO visits
VALUES (6, 3, 5, 'A', 'test')

SELECT visit_key
FROM visits
ORDER BY visit_key DESC
LIMIT 1

SELECT status_key
FROM animal
WHERE animal_id = 2

-- Selecting Animal ID (Edit Animal Entry)
SELECT animal_breed, animal_dob, arrival_cause, status_key, date_enrolled
FROM animal
WHERE animal_id = '2'

-- Updating an animal 
UPDATE animal
SET animal_breed = 'Domestic Shorthair Mix',
    animal_dob = DATE('2010-01-01'),
    arrival_cause = 'stray',
    status_key = '6',
    date_enrolled = DATE('2021-03-15')
WHERE animal_id = 7