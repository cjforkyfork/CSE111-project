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