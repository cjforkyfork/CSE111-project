SELECT animal_breed, visit_comment
FROM animal,visits
WHERE animal.animal_id = visits.animal_id
AND strftime('%Y',animal.animal_dob) < '2014'

SELECT city_name ,MAX(sums)
FROM
(SELECT city_name,SUM(money) as sums
FROM donations,shelter,city
WHERE donations.shelter_key = shelter.shelter_key
AND shelter.city_key = city.city_key
GROUP BY(city_name)
)

SELECT shelter_name
FROM shelter,city
WHERE shelter.city_key = city.city_key
AND shelter.city_key = 9

SELECT city_name, COUNT(customer_id)
FROM city, customer
WHERE customer.city_key = city.city_key
GROUP BY city_name

---------------------------------------
-- Regular Queries:

-- 1. What adoptees donated the most money and visited an animal at lease once? Don't include animals that haven't been visited.
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

-- 2. What animals haven't been visited yet, and doesn't have a request visit pending?
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

-- 7. What's the average amount of animals does each worker assist?
SELECT AVG(total)
FROM
    (SELECT COUNT(animals_assistant.animal_id) as total
    FROM shelter_assistant
        LEFT OUTER JOIN animals_assistant ON animals_assistant.assistant_id = shelter_assistant.assistant_id
    GROUP BY shelter_assistant.assistant_id)

-- 8. 