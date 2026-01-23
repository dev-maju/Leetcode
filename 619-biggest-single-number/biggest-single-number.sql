# Write your MySQL query statement below
WITH uniqueNum AS 
(SELECT num FROM MyNumbers
GROUP BY 1
HAVING COUNT(num)=1)
SELECT MAX(num) as num FROM uniqueNum;