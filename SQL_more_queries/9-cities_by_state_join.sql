-- ts is a comment
SELECT cities.id, cities.name, stat.name
FROM cities
JOIN states ON cities.state_id = states_id
ORDER BY cities.id ASC;
