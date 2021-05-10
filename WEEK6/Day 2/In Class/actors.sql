CREATE TABLE actors(
 actor_id SERIAL PRIMARY KEY,
 first_name VARCHAR (50) NOT NULL,
 last_name VARCHAR (100) NOT NULL,
 age DATE NOT NULL,
 number_oscars SMALLINT NOT NULL
)


INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Matt','Damon','08/10/1970', 5);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES(' George',' Clooney','06/05/1961 ', 2);

--SELECT * FROM producers

--UPDATE actors SET first_name = 'Johnny' , last_name ='Depp'
--WHERE actor_id = 6;


--SELECT * FROM movies

--ORDER BY actor_id;

-- CREATE TABLE producers(
-- producer_id SERIAL,
-- producer_name VARCHAR (50) NOT NULL,movie_id INTEGER,
-- PRIMARY KEY (producer_id),
-- FOREIGN KEY (movie_id) REFERENCES movies (movie_id)
-- );

-- INSERT into producers (producer_name,movie_id)
-- VALUES ('Jerry Weintraub',(SELECT movie_id FROM movies WHERE movie_title = 'Oceans Eleven'));

-- SELECT movies.movie_title, movies.movie_story
-- FROM movies
-- INNER JOIN producers
-- ON producers.producer_name = movies.movie_title;