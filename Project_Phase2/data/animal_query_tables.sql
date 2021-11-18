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
