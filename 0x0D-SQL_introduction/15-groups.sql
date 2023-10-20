-- lists number of records with same score
-- creates new colunm for number
-- lists in descending order
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
