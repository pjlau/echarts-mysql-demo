CREATE DATABASE sales_db;

USE sales_db;

CREATE TABLE sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product VARCHAR(100) NOT NULL,
    sales INT NOT NULL
);

INSERT INTO sales (product, sales) VALUES
('Product A', 120),
('Product B', 200),
('Product C', 150),
('Product D', 180),
('Product E', 90);