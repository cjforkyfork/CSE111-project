-- UPDATE not run yet

UPDATE animal
SET status_key = 1
WHERE animal_id = 10;

UPDATE visits
SET status_key = 1
WHERE visit_key = 4

-- 3. Updating animal assistant to take care of a new animal
UPDATE animals_assistant
SET animal_id = 1
WHERE assistant_id = 19