/* 
1. My partner and I want to come by each of the stores in person and meet the managers. 
Please send over the managers’ names at each store, with the full address 
of each property (street address, district, city, and country please).  
*/ 

-- staff has address_id, store_id, staff_id, first_name, last_name
-- address has address_id and everything except country
SELECT
	staff.first_name,
    staff.last_name,
    address.address,
    address.district,
    city.city,
    country.country
FROM
    store
	LEFT JOIN staff
		ON store.manager_staff_id = staff.staff_id
    LEFT JOIN address
		ON staff.address_id = address.address_id
	LEFT JOIN city
		ON address.city_id = city.city_id
	LEFT JOIN country
		ON city.country_id = country.country_id;


/*
2.	I would like to get a better understanding of all of the inventory that would come along with the business. 
Please pull together a list of each inventory item you have stocked, including the store_id number, 
the inventory_id, the name of the film, the film’s rating, its rental rate and replacement cost. 
*/

-- all inventory items: store_id, inventory_id, title, rating, rental rate, replacement cost
	-- title, rating, rental rate & replacement cost - film
    -- store_id, inventory_id - inventory
    -- connected by film_id
SELECT
	inventory.store_id,
    inventory.inventory_id,
    film.title,
    film.rating,
    film.rental_rate,
    film.replacement_cost
FROM inventory
	INNER JOIN film
		ON film.film_id = inventory.film_id;

/* 
3.	From the same list of films you just pulled, please roll that data up and provide a summary level overview 
of your inventory. We would like to know how many inventory items you have with each rating at each store. 
*/

-- agg metric - count(inventory) by rating by store
SELECT
	inventory.store_id,
    film.rating,
    COUNT(film.rating) AS rating_count
FROM inventory
	LEFT JOIN film
		ON film.film_id = inventory.film_id
GROUP BY
	inventory.store_id, 
    film.rating;

/* 
4. Similarly, we want to understand how diversified the inventory is in terms of replacement cost. We want to 
see how big of a hit it would be if a certain category of film became unpopular at a certain store.
We would like to see the number of films, as well as the average replacement cost, and total replacement cost, 
sliced by store and film category. 
*/ 

-- AVG(film.replacement_cost), SUM(film.replacement_cost) - film
-- film category - film.film_id > film_category.category_id > category.name
-- # of films - COUNT(film_id)
-- film.film_id > inventory.store_id
-- group by category (# films by cat) then store?

SELECT
-- rearranged order to put store & category first bc wanted to see metric for certain category at certain store;
-- also asked to slice (group) that way so should be organized in table column order as such
	inventory.store_id,
    category.name AS category,
    COUNT(film.film_id) AS number_movies,
    AVG(film.replacement_cost) AS avg_replacement_cost,
    SUM(film.replacement_cost) AS total_replacement_cost
FROM film
	INNER JOIN inventory
		ON inventory.film_id = film.film_id
	LEFT JOIN film_category
		ON film_category.film_id = film.film_id
	LEFT JOIN category
		ON category.category_id = film_category.category_id
GROUP BY
	inventory.store_id,
	category
ORDER BY film.avg_replacement_cost DESC; -- should be ordered by key metrics - wanted to see the metrics for replacement costs so order by replacement costs

/*
5.	We want to make sure you folks have a good handle on who your customers are. Please provide a list 
of all customer names, which store they go to, whether or not they are currently active, 
and their full addresses – street address, city, and country. 
*/

-- customer > first_name, last_name, customer_id, active, store_id, address_id 
-- address > address_id, address, city_id
-- city > city_id, city, country_id
-- country > country_id, country

SELECT
	customer.first_name,
    customer.last_name,
    address.address,
    city.city,
    country.country,
    customer.store_id,
    customer.active,
    CASE
		WHEN customer.active = 0 THEN 'inactive'
        WHEN customer.active = 1 THEN 'active'
        ELSE 'error'
	END AS active_status
FROM
	customer
    LEFT JOIN address
		ON address.address_id = customer.address_id
	LEFT JOIN city
		ON city.city_id = address.city_id
	LEFT JOIN country
		ON country.country_id = city.country_id
 ORDER BY customer.last_name, customer.first_name;

/*
6.	We would like to understand how much your customers are spending with you, and also to know 
who your most valuable customers are. Please pull together a list of customer names, their total 
lifetime rentals, and the sum of all payments you have collected from them. It would be great to 
see this ordered on total lifetime value, with the most valuable customers at the top of the list. 
*/

-- money spent by customer, most valuable customers
-- customer > customer_first_name, customer_last_name, customer_id
-- rental > count(rental_id), customer_id - group by customer_id
-- payment > rental_id, sum(amount)
-- order by total payment by customer, desc

SELECT
	customer.first_name,
    customer.last_name,
    COUNT(rental.rental_id) AS total_rentals,
    SUM(payment.amount) AS total_value
FROM
	customer
    LEFT JOIN rental
		ON rental.customer_id = customer.customer_id
	LEFT JOIN payment
		ON payment.rental_id = rental.rental_id
GROUP BY
	customer.first_name,
    customer.last_name
ORDER BY
	total_value DESC;

-- Diff's btwn my answer and key dont change output only ^ performance speed
  
/*
7. My partner and I would like to get to know your board of advisors and any current investors.
Could you please provide a list of advisor and investor names in one table? 
Could you please note whether they are an investor or an advisor, and for the investors, 
it would be good to include which company they work with. 
*/

-- advisor > first_name, last_name, advisor_id
-- investor > first_name, last_name, investor_id, company_name
-- Union then join investor.company name?

SELECT
    'investor' AS type,
    first_name,
    last_name,
    company_name
FROM
	investor
    
UNION

SELECT
	'advisor' AS type,
    first_name,
	last_name,
    NULL 
FROM
	advisor;

/*
8. We're interested in how well you have covered the most-awarded actors. 
Of all the actors with three types of awards, for what % of them do we carry a film?
And how about for actors with two types of awards? Same questions. 
Finally, how about actors with just one award? 
*/
-- Emmy, Tony, Oscar
-- actor_award > first_name, last_name, awards, actor_id

SELECT
CASE
	WHEN awards IN ('Emmy, Oscar, Tony ') THEN 'three awards'
    WHEN awards IN ('Emmy, Oscar', 'Oscar, Tony', 'Emmy, Tony') THEN 'two awards'
    ELSE 'one award'
END AS number_awards,
AVG(CASE WHEN actor_award.actor_id IS NOT NULL THEN 1 ELSE 0 END) AS perc_atleast_one_film

FROM mavenmovies.actor_award

GROUP BY
CASE
	WHEN awards IN ('Emmy, Oscar, Tony ') THEN 'three awards'
    WHEN awards IN ('Emmy, Oscar', 'Oscar, Tony', 'Emmy, Tony') THEN 'two awards'
    ELSE 'one award'
    END;