# Write your MySQL query statement below
SELECT * FROM 
(SELECT * FROM Cinema
WHERE id % 2 = 1 AND description <> 'boring' ) t
ORDER BY rating DESC;
