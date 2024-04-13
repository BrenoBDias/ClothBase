CREATE TABLE folder(
    folder_id SERIAL PRIMARY KEY,
    FOREIGN KEY(root_folder) REFERENCES folder(folder_id),
    folder_name VARCHAR( 50 ) UNIQUE NOT NULL,
    root_folder INT

);

INSERT INTO folder(folder_name,root_folder)  
VALUES  ('root', NULL),
        ('folder one', 1);


CREATE TABLE product(
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100) UNIQUE NOT NULL,
    product_description VARCHAR(500),
    created_on TIMESTAMP NOT NULL
);

CREATE TABLE custumer(
    custumer_id SERIAL PRIMARY KEY,
    custumer_name VARCHAR(50) UNIQUE NOT NULL,
    custumer_adress VARCHAR(100),
    custumer_contact_info VARCHAR(50) UNIQUE,
    custumer_email VARCHAR(50) UNIQUE,
    custumer_cpf VARCHAR(50) UNIQUE NOT NULL,
    registred_on TIMESTAMP NOT NULL,
        last_modified TIMESTAMP    
);
