# Write your MySQL query statement below
SELECT name AS customers FROM customers WHERE customers.id NOT IN (SELECT customerId FROM orders);