# Write your MySQL query statement below
select wt.id from Weather wt join Weather wy on datediff(wt.recordDate, wy.recordDate) = 1 where wt.temperature > wy.temperature;