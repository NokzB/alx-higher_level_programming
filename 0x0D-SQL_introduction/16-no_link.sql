-- lists all records of second_table
-- doesnt list rows without a name value
-- displays score and name in descending order
SELECT score, name FROM second_table WHERE name IS NOT NULL
ORDER BY score DESC;
