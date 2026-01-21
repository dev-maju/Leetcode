-- # Write your MySQL query statement below
-- SELECT name as Customers FROM Customers C
-- LEFT JOIN Orders O
-- ON C.id = O.customerId 
-- WHERE O.id IS NULL; 

SELECT name AS Customers
FROM Customers C
WHERE NOT EXISTS (
    SELECT 1
    FROM Orders O
    WHERE O.customerId = C.id
);
