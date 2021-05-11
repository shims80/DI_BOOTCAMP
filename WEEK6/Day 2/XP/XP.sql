
--Exercise 1 : Items And Customers

--SELECT * FROM items ORDER BY price;

-- SELECT * FROM items
-- ORDER BY price;

-- SELECT * FROM items WHERE price > 80;

-- SELECT first_name,last_name
-- FROM customers
-- LIMIT 3;

Exercise 2 : Dvdrental Database:

-- SELECT * FROM customer;

-- SELECT (first_name, last_name) AS full_name FROM customer;

-- SELECT DISTINCT create_date FROM customer;

-- SELECT * FROM customer ORDER BY first_name DESC;

-- SELECT film_id, title, description, release_year, rental_rate FROM film ORDER BY rental_rate;

-- SELECT address, phone FROM address WHERE district ILIKE '%Texas%';

-- SELECT  * FROM film WHERE film_id IN (15,150);

-- SELECT title FROM film;

-- SELECT film_id, title, description, length, rental_rate FROM film WHERE title ILIKE 'camelot vacation';

-- SELECT film_id, title, description, length, rental_rate FROM film WHERE title ILIKE 'ca%';

-- SELECT title, rental_rate FROM film ORDER BY rental_rate LIMIT 10;

-- SELECT title, rental_rate FROM film ORDER BY rental_rate OFFSET 10 LIMIT 10;

-- SELECT (first_name, last_name) AS full_name, amount, payment_date FROM payment INNER JOIN customer ON payment.customer_id = customer.customer_id ORDER BY payment.customer_id;

-- SELECT title FROM film LEFT JOIN inventory ON film.film_id = inventory.film_id WHERE inventory.inventory_id IS NULL ORDER BY title;

-- SELECT * FROM film WHERE title = 'Alice Fantasia';

-- SELECT * FROM inventory WHERE film_id = 14;

SELECT country, city FROM city INNER JOIN country ON country.country_id = city.country_id GROUP BY country.country, city.city ORDER BY country.country;
