CREATE DATABASE IF NOT EXISTS chatapp;
USE chatapp;

CREATE TABLE IF NOT EXISTS messageinfo (
    id INT PRIMARY KEY,
    chat_id INT,
    date_time VARCHAR(100),
    username VARCHAR(100),
    message VARCHAR(100)
);