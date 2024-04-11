CREATE DATABASE clothbase
USE clothbase

CREATE TABLE folder (
    folder_id INT PRIMARY KEY AUTO_INCREMENT,
    folder_name VARCHAR(50),
);


INSERT INTO folder
VALUES  ("ROOT"),
        ("pasta um"),
        ("pasta dois");
