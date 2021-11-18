
-- We Want to select the animal breeds and the comments they receive when they have visits for those that were born before 2014
SELECT animal_breed, visit_comment
FROM animal,visits
WHERE animal.animal_id = visits.animal_id
AND strftime('%Y',animal.animal_dob) < '2014'
GROUP BY animal_breed

-- Select the city with the highest donations among the adoptee community
SELECT city_name ,MAX(sums)
FROM
(SELECT city_name,SUM(money) as sums
FROM donations,shelter,city
WHERE donations.shelter_key = shelter.shelter_key
AND shelter.city_key = city.city_key
GROUP BY(city_name)
)

-- Select the names of the shelters that are in Ceres California
SELECT shelter_name
FROM shelter,city
WHERE shelter.city_key = city.city_key
AND shelter.city_key = 9

-- Select the city and find the number of adoptees in the city
SELECT city_name, COUNT(customer_id)
FROM city, customer
WHERE customer.city_key = city.city_key
GROUP BY city_name
