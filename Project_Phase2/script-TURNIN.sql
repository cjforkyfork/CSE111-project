-- Update Data Modification Statements --
-- 1. What adoptees donated the most money and visited an animal at lease once? Don't include animals that haven't been visited yet.
SELECT cust, MAX(Donations), TypeA as 'Animal ID'
FROM 
    (SELECT SUM(donations.money) as Donations, customer.customer_name as cust
    FROM donations 
        INNER JOIN customer ON customer.customer_id = donations.customer_id
    GROUP BY donations.customer_id),
    (SELECT customer.customer_name as Customer, animal.animal_type as 'Type of Animal', animal.animal_id as 'Animal #',COUNT(requests_visits.request_id) as 'Request Count', animal.animal_id as TypeA
    FROM customer
        INNER JOIN requests_visits ON requests_visits.customer_id = customer.customer_id
        INNER JOIN visits ON visits.animal_id = requests_visits.animal_id
        INNER JOIN animal ON animal.animal_id = visits.animal_id
    GROUP BY requests_visits.animal_id, requests_visits.customer_id
    ORDER BY requests_visits.animal_id, requests_visits.customer_id)
WHERE cust = Customer
GROUP BY TypeA
ORDER BY TypeA

-- 2. What animals haven't been visited yet, and doesn't have a request visit pending? (in otherwords, animals that haven't been engaged in interest of visiting)
SELECT animal.animal_id as 'Animal ID'
FROM animal
WHERE animal.animal_id NOT IN
    (SELECT visits.animal_id
    FROM visits
    UNION
    SELECT requests_visits.animal_id
    FROM requests_visits)

-- 3. Find the number of adoptees who had at least two donations.
SELECT donations.donation_key, customer.customer_name, COUNT(customer.customer_name) as Count, donations.money
FROM customer
    INNER JOIN donations ON donations.customer_id = customer.customer_id
GROUP BY customer.customer_id
HAVING Count > 1

-- 4. How much does each shelter community have in donations?
SELECT shelter_name, ifnull(SUM(donations.money), '0') as Donations
FROM customer_community
    LEFT OUTER JOIN shelter ON shelter.shelter_key = customer_community.shelter_key
    LEFT OUTER JOIN donations ON donations.customer_id = customer_community.customer_id
GROUP BY shelter.shelter_name

-- 5. What animal(s) are euthanized?
SELECT animal.animal_id as 'Animal ID', status.status_comment as Status
FROM animal
    INNER JOIN status ON status.status_key = animal.status_key
WHERE status_comment = 'euthanized'

-- 6. How many workers work in each shelter
SELECT COUNT(shelter_assistant.assistant_id), shelter.shelter_name
FROM shelter
    INNER JOIN shelter_assistant ON shelter_assistant.shelter_key = shelter.shelter_key
GROUP BY shelter.shelter_name

-- 7. What's the average amount of animals do each workers assist?
SELECT AVG(total)
FROM
    (SELECT COUNT(animals_assistant.animal_id) as total
    FROM shelter_assistant
        LEFT OUTER JOIN animals_assistant ON animals_assistant.assistant_id = shelter_assistant.assistant_id
    GROUP BY shelter_assistant.assistant_id)

-- 8. Find the animals that are considered to be safe to adopt. (In a kennel, or has a partner)
SELECT animal_id as Animals, status_comment as Status
FROM animal
    INNER JOIN status ON status.status_key = animal.status_key
WHERE animal.status_key = 2 OR
    animal.status_key = 6

-- 9. We Want to select the animal breeds and the comments they receive when they have visits for those that were born before 2014
SELECT animal_breed, visit_comment
FROM animal,visits
WHERE animal.animal_id = visits.animal_id
AND strftime('%Y',animal.animal_dob) < '2014'
GROUP BY animal_breed

-- 10. Select the city with the highest donations among the adoptee community
SELECT city_name ,MAX(sums)
FROM
(SELECT city_name,SUM(money) as sums
FROM donations,shelter,city
WHERE donations.shelter_key = shelter.shelter_key
AND shelter.city_key = city.city_key
GROUP BY(city_name)
)

-- 11. Select the names of the shelters that are in Ceres California
SELECT shelter_name
FROM shelter,city
WHERE shelter.city_key = city.city_key
AND shelter.city_key = 9

-- 12. Select the city and find the number of adoptees in the city
SELECT city_name, COUNT(customer_id)
FROM city, customer
WHERE customer.city_key = city.city_key
GROUP BY city_name


-- Delete Data Modification Statements --

-- 13. 
DELETE FROM 
  visits 
WHERE 
  visit_key = 3;

-- 14.
DELETE FROM 
  requests_visits 
WHERE 
  request_id = 2;


-- Insert Data Modification Statements --

-- 15. A new donation has been made.
INSERT INTO donations VALUES(13,10,16,500);

-- 16. An adoptee requested a visit with an animal
INSERT INTO requests_visits VALUES(8,5,6);

-- 17. A visit has taken place, from a pending requested visit
INSERT INTO visits VALUES(6,3,6,10,'Very likeable');


-- Update Data Modification Statements --

-- 18.
UPDATE animal
SET status_key = 1
WHERE animal_id = 10;

-- 19.
UPDATE visits
SET status_key = 1
WHERE visit_key = 4

-- 20. Updating animal assistant to take care of a new animal
UPDATE animals_assistant
SET animal_id = 1
WHERE assistant_id = 19