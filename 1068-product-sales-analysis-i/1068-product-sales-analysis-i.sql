# Write your MySQL query statement below
select Product.product_name, Sales.year, Sales.price
from Sales
LEFT JOIN product
ON Sales.product_id = product.product_id
