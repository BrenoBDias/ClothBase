CREATE TABLE folder(
    folder_id SERIAL PRIMARY KEY,
    root_folder INT,
    FOREIGN KEY(root_folder) REFERENCES folder(folder_id),
    folder_name VARCHAR( 50 ) UNIQUE NOT NULL

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

INSERT INTO product(product_name, product_description, created_on)
VALUES  ('Blue button', NULL, CURRENT_TIMESTAMP),
        ('Black fabric', 'cotton', CURRENT_TIMESTAMP),
        ('Pink fabric', 'detailed with yellow circles', CURRENT_TIMESTAMP),
        ('White fabric', NULL, CURRENT_TIMESTAMP);


CREATE TABLE custumer(
    custumer_id SERIAL PRIMARY KEY,
    custumer_name VARCHAR(50) UNIQUE NOT NULL,
    custumer_adress VARCHAR(100),
    custumer_contact_info VARCHAR(50) UNIQUE,
    custumer_email VARCHAR(50) UNIQUE,
    custumer_cpf CHAR(11) UNIQUE NOT NULL,
    registred_on TIMESTAMP NOT NULL,
        last_modified TIMESTAMP
);

INSERT INTO custumer(custumer_name, custumer_adress, custumer_contact_info, custumer_email, custumer_cpf, registred_on)
VALUES  ('Larry Lobster', 'Bikini Bottom', '9999-9999', 'larryTheLobster@mail.com', '12345678901', CURRENT_TIMESTAMP),
        ('Sandy Cheeks', 'Bikini Bottom', '9999-9998', 'SandyCheeks@mail.com', '12345678902', CURRENT_TIMESTAMP),
        ('Pearl Krabs', 'Bikini Bottom', '9999-9997', 'Pearl@mail.com', '12345678903', CURRENT_TIMESTAMP);
        

CREATE TABLE project(
    project_id SERIAL PRIMARY KEY UNIQUE NOT NULL,
    custumer_id INT,
    FOREIGN KEY(custumer_id) REFERENCES custumer(custumer_id),
    project_name VARCHAR(50) UNIQUE,
    project_description VARCHAR(500),
    registred_on TIMESTAMP NOT NULL,
        last_modified TIMESTAMP
);

INSERT INTO project(custumer_id, project_name, project_description, registred_on)
VALUES  (2, 'A Summer evening', 'pink dress with yellow circles', CURRENT_TIMESTAMP),
        (1, 'Full Black Ecobag', NULL, CURRENT_TIMESTAMP),
        (2, 'White Ecobag', NULL,CURRENT_TIMESTAMP);


CREATE TABLE stock_out(
    stock_out_id SERIAL PRIMARY KEY UNIQUE NOT NULL,
    product_id INT NOT NULL,
    FOREIGN KEY (product_id) REFERENCES product(product_id),
    project_id INT NOT NULL,
    FOREIGN KEY (project_id) REFERENCES project(project_id),
    stock_out_quantity INT NOT NULL,
    registred_on TIMESTAMP NOT NULL
);

INSERT INTO stock_out(product_id, project_id, stock_out_quantity, registred_on)
VALUES  (3, 1, 1, CURRENT_TIMESTAMP),
        (1, 1, 5, CURRENT_TIMESTAMP),
        (2, 2, 1, CURRENT_TIMESTAMP),
        (4, 3, 1, CURRENT_TIMESTAMP);


CREATE TABLE image(
    image_id SERIAL PRIMARY KEY UNIQUE NOT NULL,
    product_id INT,
    FOREIGN KEY (product_id) REFERENCES product(product_id),
    project_id INT,
    FOREIGN KEY (project_id) REFERENCES project(project_id),
    image_data INT NOT NULL,
    registred_on TIMESTAMP NOT NULL
);

INSERT INTO image(product_id, project_id, image_data, registred_on)
VALUES  (NULL, 1, 1, CURRENT_TIMESTAMP),
        (1, NULL, 1, CURRENT_TIMESTAMP),
        (NULL, 2, 1, CURRENT_TIMESTAMP),
        (NULL, 3, 1, CURRENT_TIMESTAMP),
        (3, NULL, 1, CURRENT_TIMESTAMP),
        (3, NULL, 1, CURRENT_TIMESTAMP);
            


CREATE TABLE tag(
    tag_id SERIAL PRIMARY KEY UNIQUE NOT NULL,
    product_id INT,
    FOREIGN KEY (product_id) REFERENCES product(product_id),
    project_id INT,
    FOREIGN KEY (project_id) REFERENCES project(project_id),
    tag_name VARCHAR (50)
);

INSERT INTO tag(product_id, project_id, tag_name)
VALUES  (3, 1, 'pink'),
        (3, NULL, 'detailed fabric'),
        (2, NULL, 'not datailed fabric'),    
        (4, NULL, 'not datailed fabric'),
        (NULL, 2, 'full black projects');


CREATE TABLE supplier(
    supplier_id SERIAL PRIMARY KEY UNIQUE NOT NULL,
    supplier_name VARCHAR(50) UNIQUE NOT NULL,
    supplier_contact_info VARCHAR (50),
    supplier_adress VARCHAR(100),
    supplier_email VARCHAR(50) UNIQUE,
    supplier_site VARCHAR(50) UNIQUE,
    registred_on TIMESTAMP NOT NULL,
        last_modified TIMESTAMP
);

INSERT INTO supplier(supplier_name, supplier_contact_info, supplier_adress, supplier_email, supplier_site, registred_on)
VALUES  ('krusty krab', '1824-4187', 'Bikini Bottom', 'krustyk@mail.com', 'krustykrabs.com', CURRENT_TIMESTAMP),
        ('Chum bucket', '1293-1298', 'Bikini Bottom', 'sheldonjplankton@chumbucket.com','chumbuket.com', CURRENT_TIMESTAMP);    


CREATE TABLE stock_in(
    stock_in_id SERIAL PRIMARY KEY UNIQUE NOT NULL,
    product_id INT,
    FOREIGN KEY (product_id) REFERENCES product(product_id),
    supplier_id INT,
    FOREIGN KEY (supplier_id) REFERENCES supplier(supplier_id),
    stock_in_quantity INT NOT NULL,
    stock_in_unit_price NUMERIC(5,2),
    registred_on TIMESTAMP NOT NULL

);

INSERT INTO stock_in(product_id, supplier_id, stock_in_quantity, stock_in_unit_price, registred_on)
VALUES  (3, 1, 10, 9.99, CURRENT_TIMESTAMP),
        (1, 1, 50, 2.99, CURRENT_TIMESTAMP),
        (2, 2, 10, 5.99, CURRENT_TIMESTAMP),
        (4, 2, 10, 3.54, CURRENT_TIMESTAMP);  
