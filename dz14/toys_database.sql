-- Створення таблиці "toys"
CREATE TABLE toys (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    type TEXT,
    price REAL,
    stock_quantity INTEGER
);

INSERT INTO toys (name, type, price, stock_quantity) VALUES
    ('Teddy Bear', 'Plush', 15.99, 20),
    ('Doll', 'Soft', 25.49, 15),
    ('Stuffed Elephant', 'Plush', 18.99, 12),
    ('Toy Bunny', 'Soft', 12.79, 8);

SELECT name FROM toys;

SELECT name, price FROM toys WHERE price < 20;

SELECT type, SUM(stock_quantity) as total_quantity FROM toys GROUP BY type;

SELECT name, stock_quantity FROM toys WHERE stock_quantity < 10;

DELETE FROM toys WHERE stock_quantity <= 0;

UPDATE toys SET stock_quantity = stock_quantity + 5 WHERE name = 'Teddy Bear';
