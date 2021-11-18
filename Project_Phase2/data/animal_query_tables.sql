SELECT * 
FROM animal;

SELECT assistant_id,COUNT(animal_id)
FROM animals_assistant
GROUP BY assistant_id;

SELECT MAX(money)
FROM donations;

