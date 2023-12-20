
SELECT name FROM users WHERE email LIKE '%@gmail.com%';

SELECT * FROM toys ORDER BY price DESC;

SELECT t.name, COUNT(o.order_id) as order_count
FROM toys t
LEFT JOIN orders o ON t.id = o.toy_id
GROUP BY t.name;

SELECT AVG(price) as average_price FROM toys;

SELECT MAX(price) as max_price FROM toys;

SELECT MIN(stock_quantity) as min_stock FROM toys;

SELECT
    name,
    price,
    CASE
        WHEN price < 10 THEN 'Економний'
        WHEN price BETWEEN 10 AND 20 THEN 'Середній'
        WHEN price BETWEEN 20 AND 30 THEN 'Високий'
        ELSE 'Дуже високий'
    END as price_category
FROM toys;

SELECT
    name,
    stock_quantity,
    CASE
        WHEN stock_quantity > 50 THEN '10%'
        WHEN stock_quantity BETWEEN 20 AND 50 THEN '5%'
        ELSE 'Без знижки'
    END as discount
FROM toys;
