-- Query all animals
SELECT animal_id, animal_type, animal_breed, animal_dob, arrival_cause, status_comment, date_enrolled
FROM animal
    INNER JOIN status ON status.status_key = animal.status_key