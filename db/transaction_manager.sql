DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS merchands;
DROP TABLE IF EXISTS tags;

CREATE TABLE merchands (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    amount FLOAT,
    merchand_id INT REFERENCES merchands(id),
    tag_id INT REFERENCES tags(id)
);