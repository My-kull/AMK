SELECT country.name AS "country name", airport.name AS "airport name"
FROM country
JOIN airport ON country.iso_country = airport.iso_country
WHERE airport.scheduled_service = 'yes' AND country.name = 'Finland';

SELECT game.screen_name, airport.name
FROM game
JOIN airport ON game.location = airport.ident;

SELECT game.screen_name, country.name
FROM game
JOIN airport ON game.location = airport.ident
JOIN country ON country.iso_country = airport.iso_country
WHERE airport.ident = game.location;

SELECT airport.name, game.screen_name
FROM airport
LEFT JOIN game ON game.location = airport.ident
WHERE airport.name LIKE '%Hels%';

SELECT goal.name, game.screen_name
FROM goal
LEFT JOIN goal_reached ON goal.id = goal_reached.goal_id
LEFT JOIN game ON game.id = goal_reached.game_id;

SELECT country.name
FROM country
JOIN airport ON country.iso_country = airport.iso_country
WHERE airport.name LIKE 'Satsuma%';

SELECT airport.name
FROM airport
JOIN country ON country.iso_country = airport.iso_country
WHERE country.name = 'Monaco';

SELECT game.screen_name
FROM game
JOIN goal_reached ON game.id = goal_reached.game_id
JOIN goal ON goal.id = goal_reached.goal_id
WHERE goal.name = 'CLOUDS';

SELECT country.name
FROM country
LEFT JOIN airport ON country.iso_country = airport.iso_country
WHERE airport.iso_country IS NULL;

SELECT goal.name
FROM goal
LEFT JOIN goal_reached ON goal.id = goal_reached.goal_id
AND goal_reached.game_id IN (SELECT game.id FROM game WHERE game.screen_name = 'Heini')
WHERE goal_reached.goal_id IS NULL;

SELECT max(elevation_ft)
FROM airport;

SELECT country.continent, count(*)
FROM country
JOIN airport ON country.iso_country = airport.iso_country
GROUP BY country.continent;

SELECT country.continent, count(*)
FROM country
GROUP BY country.continent;

SELECT game.screen_name, count(*)
FROM game
JOIN goal_reached ON game.id = goal_reached.game_id
GROUP BY game.screen_name;

SELECT game.screen_name
FROM game
ORDER BY game.co2_consumed ASC
LIMIT 1;

SELECT country.name, count(*)
FROM country
JOIN airport ON country.iso_country = airport.iso_country
GROUP BY country.name
ORDER BY COUNT(airport.id) DESC, airport.name DESC
LIMIT 50;

SELECT country.name
FROM country
JOIN airport ON country.iso_country = airport.iso_country
GROUP BY country.name
HAVING COUNT(airport.id) > 1000
ORDER BY country.iso_country;

SELECT airport.name
FROM airport
ORDER BY airport.elevation_ft DESC
LIMIT 1;

SELECT country.name
FROM country
JOIN airport ON country.iso_country = airport.iso_country
WHERE airport.id = (SELECT id FROM airport ORDER BY elevation_ft DESC LIMIT 1);

SELECT count(*)
FROM goal_reached
JOIN game ON game.id = goal_reached.game_id
WHERE game.screen_name = 'Vesa';

SELECT airport.name
FROM airport
ORDER BY ABS(airport.latitude_deg) DESC
LIMIT 1;

UPDATE game
SET location = (SELECT ident FROM airport WHERE name = 'Nottingham Airport'),
    co2_consumed = co2_consumed + 500
WHERE screen_name = 'Vesa';

DELETE FROM goal_reached;

DELETE FROM game;
