-- # Write your MySQL query statement below
-- WITH uniqueNum AS 
-- (SELECT num FROM MyNumbers
-- GROUP BY 1
-- HAVING COUNT(num)=1)
-- SELECT MAX(num) as num FROM uniqueNum;

SELECT MAX(num) AS num
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
) t;

