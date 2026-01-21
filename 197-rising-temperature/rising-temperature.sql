-- # Write your MySQL query statement below
-- SELECT P2.id FROM Weather P1 
-- JOIN Weather P2
-- ON P2.recordDate = DATE_ADD(P1.recordDate, INTERVAL 1 DAY)
-- WHERE P2.temperature>P1.temperature;


SELECT w2.id
FROM Weather w2
JOIN Weather w1
ON w1.recordDate = DATE_SUB(w2.recordDate, INTERVAL 1 DAY)
WHERE w2.temperature > w1.temperature;
