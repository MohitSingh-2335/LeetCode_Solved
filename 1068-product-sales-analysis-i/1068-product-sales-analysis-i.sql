# Write your MySQL query statement below
select pt.product_name, st.year, st.price
from Product pt
right join Sales st
on pt.product_id = st.product_id