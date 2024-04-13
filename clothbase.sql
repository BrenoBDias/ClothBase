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

CREATE TABLE project(
    project_id SERIAL PRIMARY KEY UNIQUE NOT NULL,
    custumer_id INT,
    FOREIGN KEY(custumer_id) REFERENCES custumer(custumer_id),
    project_name VARCHAR(50) UNIQUE,
    project_description VARCHAR(500),
    registred_on TIMESTAMP NOT NULL,
        last_modified TIMESTAMP
);

CREATE TABLE stock_out(
    stock_out_id SERIAL PRIMARY KEY UNIQUE NOT NULL,
    product_id INT NOT NULL,
    FOREIGN KEY (product_id) REFERENCES product(product_id),
    project_id INT NOT NULL,
    FOREIGN KEY (project_id) REFERENCES project(project_id),
    stock_out_quantity INT NOT NULL,
    registred_on TIMESTAMP NOT NULL
);

CREATE TABLE image(
    image_id SERIAL PRIMARY KEY UNIQUE NOT NULL,
    product_id INT,
    FOREIGN KEY (product_id) REFERENCES product(product_id),
    project_id INT,
    FOREIGN KEY (project_id) REFERENCES project(project_id),
    image_data INT NOT NULL,
    registred_on TIMESTAMP NOT NULL
);

CREATE TABLE tag(
    tag_id SERIAL PRIMARY KEY UNIQUE NOT NULL,
    product_id INT,
    FOREIGN KEY (product_id) REFERENCES product(product_id),
    project_id INT,
    FOREIGN KEY (project_id) REFERENCES project(project_id),
    tag_name VARCHAR (15)
);

CREATE TABLE supplier(
    supplier_id SERIAL PRIMARY KEY UNIQUE NOT NULL,
    supplier_name VARCHAR(50) UNIQUE NOT NULL,
    supplier_contact_info VARCHAR (50),
    supplier_adress VARCHAR(100) UNIQUE,
    supplier_email VARCHAR(50) UNIQUE,
    supplier_site VARCHAR(50) UNIQUE,
    registred_on TIMESTAMP NOT NULL,
        last_modified TIMESTAMP
);

CREATE TABLE stock_in(
    stock_in_id SERIAL PRIMARY KEY UNIQUE NOT NULL,
    product_id INT,
    FOREIGN KEY (product_id) REFERENCES product(product_id),
    project_id INT,
    FOREIGN KEY (project_id) REFERENCES project(project_id),
    quantity INT NOT NULL,
    stock_in_unit_price NUMERIC(5,2)

);