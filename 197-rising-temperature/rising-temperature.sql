# Write your MySQL query statement below
SELECT P2.id FROM Weather P1 
JOIN Weather P2
ON P2.recordDate = DATE_ADD(P1.recordDate, INTERVAL 1 DAY)
WHERE P2.temperature>P1.temperature;
