# Write your MySQL query statement below
select p.firstname, p.lastname, s.city, s.state
from person p
left join address s
on p.personid = s.personid;